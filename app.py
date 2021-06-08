import sys
from validador import valida_cnpj
from gerador import gera_cnpj
from PyQt5.QtWidgets import QApplication, QMainWindow
import design


class GeraValidaCNPJ(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCNPJ.clicked.connect(self.gera_cnpj)
        self.btnValidaCNPJ.clicked.connect(self.valida_cnpj)

    def gera_cnpj(self):
        self.inputValidaCNPJ.setText(
            str(gera_cnpj())
        )

    def valida_cnpj(self):
        cnpj = self.inputValidaCNPJ.text()
        self.inputRetorno.setText(
            str(valida_cnpj(cnpj))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cnpj = GeraValidaCNPJ()
    gera_valida_cnpj.show()
    qt.exec_()
