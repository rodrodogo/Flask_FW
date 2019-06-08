import unittest
import sys
print(sys.path)
from ../(app.Gestor import *



class Test(unittest.TestCase):

    def test_insertP(self):
        db = DtoPerson()
        camila = Person(identification = 1, name = 'camila', age = 32)
        db.insert(camila)
        result = db.queryByName('camila')
        self.assertEqual(result.name, camila.name)
        db.delete(camila.identification)

    def test_updateP(self):
        db = DtoPerson()
        camila = Person(identification = 1, name = 'camila', age = 32)
        db.insert(camila)
        camila.name = "camilo"
        db.update(camila)
        result = db.queryByName('camilo')
        self.assertEqual(result.identification, camila.identification)
        db.delete(camila.identification)

    def test_insertG(self):
        db = DtoGroups()
        ud = Group(id = 1, name = 'udistrital')
        db.insert(ud)
        result = db.queryByName('ud')
        self.assertEqual(result.name, ud.name)
        db.delete(ud.id)

    def test_updateG(self):
        db = DtoGroups()
        ud = Group(ud = 1, name = 'udistrital')
        db.insert(camila)
        ud.name = "udin"
        db.update(ud)
        result = db.queryByName('udin')
        self.assertEqual(result.id, camila.id)
        db.delete(ud.id)

if __name__ == '__main__':
    unittest.main()
