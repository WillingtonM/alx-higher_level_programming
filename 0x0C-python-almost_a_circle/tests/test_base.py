#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def tests_no_arg(self):
        bsz1 = Base()
        bsz2 = Base()
        self.assertEqual(bsz1.id, bsz2.id - 1)

    def tests_3_bases(self):
        bsz1 = Base()
        bsz2 = Base()
        bsz3 = Base()
        self.assertEqual(bsz1.id, bsz3.id - 2)

    def tests_None_id(self):
        bsz1 = Base(None)
        bsz2 = Base(None)
        self.assertEqual(bsz1.id, bsz2.id - 1)

    def tests_nb_instances_after_unique_id(self):
        bsz1 = Base()
        bsz2 = Base(12)
        bsz3 = Base()
        self.assertEqual(bsz1.id, bsz3.id - 1)

    def tests_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def tests_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def tests_id_public(self):
        bs = Base(12)
        bs.id = 15
        self.assertEqual(15, bs.id)
    
    def tests_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def tests_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def tests_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def tests_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def tests_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def tests_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def tests_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def tests_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def tests_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def tests_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def tests_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def tests_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def tests_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def tests_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def tests_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def tests_2_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests testing to_json_string method of Base class."""

    def tests_to_json_string_rectangle_type(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def tests_to_json_string_rectangle_1_dict(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def tests_to_json_string_rectangle_2_dicts(self):
        rct1 = Rectangle(2, 3, 5, 19, 2)
        rct2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rct1.to_dictionary(), rct2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def tests_to_json_string_square_type(self):
        sqr = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

    def tests_to_json_string_square_1_dict(self):
        sqr = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sqr.to_dictionary()])) == 39)

    def tests_to_json_string_square_2_dicts(self):
        sz1 = Square(10, 2, 3, 4)
        sz2 = Square(4, 5, 21, 2)
        list_dicts = [sz1.to_dictionary(), sz2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def tests_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def tests_to_json_string_n1(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def tests_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def tests_to_json_string_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def tests_save_to_file_1_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def tests_save_to_file_2_rectangles(self):
        rct1 = Rectangle(10, 7, 2, 8, 5)
        rct2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rct1, rct2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def tests_save_to_file_1_square(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def tests_save_to_file_2_squares(self):
        sz1 = Square(10, 7, 2, 8)
        sz2 = Square(8, 1, 2, 3)
        Square.save_to_file([sz1, sz2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def tests_save_to_file_cls_name_for_filename(self):
        sqr = Square(10, 7, 2, 8)
        Base.save_to_file([sqr])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def tests_save_to_file_overwrite(self):
        sqr = Square(9, 2, 39, 2)
        Square.save_to_file([sqr])
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def tests_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def tests_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def tests_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def tests_save_to_file_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class"""

    def tests_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_outpt = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_outpt))

    def tests_from_json_string_1_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_outpt = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_outpt)

    def tests_from_json_string_2_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_outpt = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_outpt)

    def tests_from_json_string_1_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_outpt = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_outpt)

    def tests_from_json_string_2_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_outpt = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_outpt)

    def tests_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def tests_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def tests_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def tests_from_json_string_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class"""

    def tests_create_rectangle_original(self):
        rct1 = Rectangle(3, 5, 1, 2, 7)
        rct1_dictionary = rct1.to_dictionary()
        rct2 = Rectangle.create(**rct1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rct1))

    def tests_create_rectangle_new(self):
        rct1 = Rectangle(3, 5, 1, 2, 7)
        rct1_dictionary = rct1.to_dictionary()
        rct2 = Rectangle.create(**rct1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rct2))

    def tests_create_rectangle_is(self):
        rct1 = Rectangle(3, 5, 1, 2, 7)
        rct1_dictionary = rct1.to_dictionary()
        rct2 = Rectangle.create(**rct1_dictionary)
        self.assertIsNot(rct1, rct2)

    def tests_create_rectangle_equals(self):
        rct1 = Rectangle(3, 5, 1, 2, 7)
        rct1_dictionary = rct1.to_dictionary()
        rct2 = Rectangle.create(**rct1_dictionary)
        self.assertNotEqual(rct1, rct2)

    def tests_create_square_original(self):
        sz1 = Square(3, 5, 1, 7)
        sz1_dictionary = sz1.to_dictionary()
        sz2 = Square.create(**sz1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sz1))

    def tests_create_square_new(self):
        sz1 = Square(3, 5, 1, 7)
        sz1_dictionary = sz1.to_dictionary()
        sz2 = Square.create(**sz1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sz2))

    def tests_create_square_is(self):
        sz1 = Square(3, 5, 1, 7)
        sz1_dictionary = sz1.to_dictionary()
        sz2 = Square.create(**sz1_dictionary)
        self.assertIsNot(sz1, sz2)

    def tests_create_square_equals(self):
        sz1 = Square(3, 5, 1, 7)
        sz1_dictionary = sz1.to_dictionary()
        sz2 = Square.create(**sz1_dictionary)
        self.assertNotEqual(sz1, sz2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def tests_load_from_file_first_rectangle(self):
        rct1 = Rectangle(10, 7, 2, 8, 1)
        rct2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rct1, rct2])
        list_rectangles_outpt = Rectangle.load_from_file()
        self.assertEqual(str(rct1), str(list_rectangles_outpt[0]))

    def tests_load_from_file_second_rectangle(self):
        rct1 = Rectangle(10, 7, 2, 8, 1)
        rct2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rct1, rct2])
        list_rectangles_outpt = Rectangle.load_from_file()
        self.assertEqual(str(rct2), str(list_rectangles_outpt[1]))

    def tests_load_from_file_rectangle_types(self):
        rct1 = Rectangle(10, 7, 2, 8, 1)
        rct2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rct1, rct2])
        outpt = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in outpt))

    def tests_load_from_file_first_square(self):
        sz1 = Square(5, 1, 3, 3)
        sz2 = Square(9, 5, 2, 3)
        Square.save_to_file([sz1, sz2])
        list_squares_outpt = Square.load_from_file()
        self.assertEqual(str(sz1), str(list_squares_outpt[0]))

    def tests_load_from_file_second_square(self):
        sz1 = Square(5, 1, 3, 3)
        sz2 = Square(9, 5, 2, 3)
        Square.save_to_file([sz1, sz2])
        list_squares_outpt = Square.load_from_file()
        self.assertEqual(str(sz2), str(list_squares_outpt[1]))

    def tests_load_from_file_square_types(self):
        sz1 = Square(5, 1, 3, 3)
        sz2 = Square(9, 5, 2, 3)
        Square.save_to_file([sz1, sz2])
        outpt = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in outpt))

    def tests_load_from_file_no_file(self):
        outpt = Square.load_from_file()
        self.assertEqual([], outpt)

    def tests_load_from_file_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def tests_save_to_file_csv_1_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def tests_save_to_file_csv_2_rectangles(self):
        rct1 = Rectangle(10, 7, 2, 8, 5)
        rct2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rct1, rct2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def tests_save_to_file_csv_1_square(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def tests_save_to_file_csv_2_squares(self):
        sz1 = Square(10, 7, 2, 8)
        sz2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sz1, sz2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def tests_save_to_file__csv_cls_name(self):
        sqr = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sqr])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def tests_save_to_file_csv_overwrite(self):
        sqr = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sqr])
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def tests_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def tests_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def tests_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def tests_save_to_file_csv_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def tests_load_from_file_csv_first_rectangle(self):
        rct1 = Rectangle(10, 7, 2, 8, 1)
        rct2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rct1, rct2])
        list_rectangles_outpt = Rectangle.load_from_file_csv()
        self.assertEqual(str(rct1), str(list_rectangles_outpt[0]))

    def tests_load_from_file_csv_second_rectangle(self):
        rct1 = Rectangle(10, 7, 2, 8, 1)
        rct2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rct1, rct2])
        list_rectangles_outpt = Rectangle.load_from_file_csv()
        self.assertEqual(str(rct2), str(list_rectangles_outpt[1]))

    def tests_load_from_file_csv_rectangle_types(self):
        rct1 = Rectangle(10, 7, 2, 8, 1)
        rct2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rct1, rct2])
        outpt = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in outpt))

    def tests_load_from_file_csv_first_square(self):
        sz1 = Square(5, 1, 3, 3)
        sz2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sz1, sz2])
        list_squares_outpt = Square.load_from_file_csv()
        self.assertEqual(str(sz1), str(list_squares_outpt[0]))

    def tests_load_from_file_csv_second_square(self):
        sz1 = Square(5, 1, 3, 3)
        sz2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sz1, sz2])
        list_squares_outpt = Square.load_from_file_csv()
        self.assertEqual(str(sz2), str(list_squares_outpt[1]))

    def tests_load_from_file_csv_square_types(self):
        sz1 = Square(5, 1, 3, 3)
        sz2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sz1, sz2])
        outpt = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in outpt))

    def tests_load_from_file_csv_no_file(self):
        outpt = Square.load_from_file_csv()
        self.assertEqual([], outpt)

    def tests_load_from_file_csv_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()
