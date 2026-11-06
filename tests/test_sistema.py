import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from sistema import carregar,buscar,consultar
RAIZ=Path(__file__).resolve().parents[1]
class Testes(unittest.TestCase):
 def setUp(self):self.base=carregar(RAIZ/'data'/'base.json')
 def test_quantidade(self):self.assertGreaterEqual(len(self.base),15);self.assertGreaterEqual(len({r['tema'] for r in self.base}),3)
 def test_vazio(self):self.assertEqual(buscar('',self.base)['status'],'invalida')
 def test_fora_base(self):self.assertEqual(buscar('Como solicitar licença para construir em Marte?',self.base)['status'],'sem_resposta')
 def test_tema_invalido(self):self.assertEqual(buscar('CPF',self.base,'tema inexistente')['status'],'invalida')
 def test_arquivo_ausente(self):
  with self.assertRaises(ValueError):carregar('/arquivo/inexistente.json')
 def test_arquivo_vazio(self):
  with tempfile.TemporaryDirectory() as d:
   x=Path(d)/'base.json';x.write_text('[]');
   with self.assertRaises(ValueError):carregar(x)
 def test_json_corrompido(self):
  with tempfile.TemporaryDirectory() as d:
   x=Path(d)/'base.json';x.write_text('{');
   with self.assertRaises(ValueError):carregar(x)
 def test_gratuidade_gov(self):
  self.assertEqual(buscar('A conta GOV.BR é gratuita?',self.base)['registro']['id'],'ORI-015')
 def test_consulta_ambigua_documentos(self):
  self.assertEqual(buscar('identidade cpf',self.base)['status'],'ambigua')
 def test_modelos_resposta(self):
  a=consultar('O que é uma conta GOV.BR?',self.base,modelo='A')['texto']
  b=consultar('O que é uma conta GOV.BR?',self.base,modelo='B')['texto']
  self.assertIn('Fonte:',a)
  self.assertIn('VERIFICAÇÃO:',b)
  self.assertIn('ATENÇÃO:',b)
 def test_referencia(self):
  r=consultar('O que é uma conta GOV.BR?',self.base)
  self.assertEqual(r['status'],'ok');self.assertIn('FONTE:',r['texto'])
if __name__=='__main__':unittest.main()
