from veiculo_pai import Veiculo

class Onibus(Veiculo):
        def capacidade_assentos(self, capacidade = 30):
                return super().capacidade_assentos(capacidade)

onibus_escolar = Onibus("Scania", 120, 15);
onibus_escolar.toStr();
onibus_escolar.capacidade_assentos();