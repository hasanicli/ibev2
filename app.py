import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAction
from screens import *


class App(MainWindow):
    def __init__(self):
        super().__init__()

        # Triggered signals
        self.ui.act_class.triggered.connect(lambda: self.open(ClassWindow))
        self.ui.act_add_class_to_parent.triggered.connect(lambda: self.open(AddClassWindow))
        self.ui.act_branch.triggered.connect(lambda: self.open(BranchWindow))
        self.ui.act_degree.triggered.connect(lambda: self.open(DegreeWindow))
        self.ui.act_department.triggered.connect(lambda: self.open(DepartmentWindow))
        self.ui.act_institutation_info.triggered.connect(lambda: self.open(InstitutionWindow))
        self.ui.act_staff_branch.triggered.connect(lambda: self.open(StaffBranchWindow))
        self.ui.act_staff.triggered.connect(lambda: self.open(StaffWindow))
        self.ui.act_student.triggered.connect(lambda: self.open(StudentWindow))
        self.ui.act_workplace.triggered.connect(lambda: self.open(WorkplaceWindow))
        self.ui.act_neighborhood.triggered.connect(lambda:self.open(NeighborhoodWindow))
        self.ui.act_cause.triggered.connect(lambda: self.open(CauseWindow))
        self.ui.act_parent_class.triggered.connect(lambda: self.open(ParentClassWindow))
        self.ui.act_staff_workplace.triggered.connect(lambda: self.open(AddWorkplaceToStaff))
        self.ui.act_day.triggered.connect(lambda: self.open(DayWindow))
        self.ui.act_change_workplace.triggered.connect(lambda: self.open(ChangeWorkplaceWindow))
        self.ui.act_disconnection.triggered.connect(lambda: self.open(DisconnectionWindow))

    def open(self, param_class):
        self.inst = param_class()
        self.inst.setWindowModality(Qt.ApplicationModal)
        self.inst.show()


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())
