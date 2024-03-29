#!/usr/bin/python3
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation - line 22
    TestSquare_size - line 86
    TestSquare_x - line 164
    TestSquare_y - line 236
    TestSquare_order_of_initialization - line 304
    TestSquare_area - line 320
    TestSquare_stdout - line 341
    TestSquare_update_args - line 424
    TestSquare_update_kwargs - line 536
    TestSquare_to_dictionary - 638
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square

class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of Square class"""

    def tests_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def tests_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def tests_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def tests_1_arg(self):
        sz1 = Square(10)
        sz2 = Square(11)
        self.assertEqual(sz1.id, sz2.id - 1)

    def tests_2_args(self):
        sz1 = Square(10, 2)
        sz2 = Square(2, 10)
        self.assertEqual(sz1.id, sz2.id - 1)

    def tests_3_args(self):
        sz1 = Square(10, 2, 2)
        sz2 = Square(2, 2, 10)
        self.assertEqual(sz1.id, sz2.id - 1)

    def tests_4_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def tests_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def tests_more_than_4_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def tests_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def tests_size_setter(self):
        sqr = Square(4, 1, 9, 2)
        sqr.size = 8
        self.assertEqual(8, sqr.size)

    def tests_height_getter(self):
        sqr = Square(4, 1, 9, 2)
        sqr.size = 8
        self.assertEqual(8, sqr.height)

    def tests_width_getter(self):
        sqr = Square(4, 1, 9, 2)
        sqr.size = 8
        self.assertEqual(8, sqr.width)

    def tests_y_getter(self):
        self.assertEqual(0, Square(10).y)

    def tests_x_getter(self):
        self.assertEqual(0, Square(10).x)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of Square class"""

    def tests_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def tests_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def tests_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def tests_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def tests_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def tests_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def tests_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def tests_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def tests_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def tests_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def tests_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def tests_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def tests_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def tests_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def tests_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def tests_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def tests_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def tests_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def tests_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def tests_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def tests_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def tests_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def tests_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def tests_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def tests_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def tests_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def tests_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})


    def tests_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def tests_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def tests_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def tests_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def tests_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def tests_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def tests_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def tests_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def tests_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def tests_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def tests_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def tests_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def tests_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def tests_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def tests_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def tests_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def tests_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def tests_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def tests_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def tests_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    def tests_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def tests_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def tests_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)

    def tests_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def tests_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def tests_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def tests_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing area method of Square class"""

    def tests_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def tests_area_large(self):
        sqr = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, sqr.area())

    def tests_area_changed_attributes(self):
        sqr = Square(2, 0, 0, 1)
        sqr.size = 7
        self.assertEqual(49, sqr.area())

    def tests_area_1_arg(self):
        sqr = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            sqr.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class"""

    @staticmethod
    def capture_stdout(sq, method):
        """
            Captures and returns text printed to stdout.

            Args:
                sq (Square): Square ot print to stdout.
                method (str): Method to run on sq.
            Returns:
                Text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def tests_str_method_print_size(self):
        sqr = Square(4)
        capture = TestSquare_stdout.capture_stdout(sqr, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(sqr.id)
        self.assertEqual(correct, capture.getvalue())

    def tests_str_method_size_x(self):
        sqr = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(sqr.id)
        self.assertEqual(correct, sqr.area__str__())

    def tests_str_method_size_x_y(self):
        sqr = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def tests_str_method_size_x_y_id(self):
        sqr = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sqr))

    def tests_str_method_changed_attributes(self):
        sqr = Square(7, 0, 0, [4])
        sqr.size = 15
        sqr.x = 8
        sqr.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(sqr))

    def tests_str_method_1_arg(self):
        sqr = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            sqr.__str__(1)

    # Test display method
    def tests_display_size(self):
        sqr = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(sqr, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def tests_display_size_x(self):
        sqr = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(sqr, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def tests_display_size_y(self):
        sqr = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(sqr, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def tests_display_size_x_y(self):
        sqr = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(sqr, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def tests_display_1_arg(self):
        sqr = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sqr.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of Square class"""

    def tests_update_args_zero(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sqr))

    def tests_update_args_1(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(sqr))

    def tests_update_args_2(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sqr))

    def tests_update_args_3(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(sqr))

    def tests_update_args_4(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqr))

    def tests_update_args_more_than_4(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqr))

    def tests_update_args_width_setter(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2)
        self.assertEqual(2, sqr.width)

    def tests_update_args_height_setter(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2)
        self.assertEqual(2, sqr.height)

    def tests_update_args_None_id(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def tests_update_args_None_id_and_more(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def tests_update_args_twice(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, 3, 4)
        sqr.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(sqr))

    def tests_update_args_invalid_size_type(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(89, "invalid")

    def tests_update_args_size_zero(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(89, 0)

    def tests_update_args_size_negative(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(89, -4)

    def tests_update_args_invalid_x(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(89, 1, "invalid")

    def tests_update_args_x_negative(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.update(98, 1, -4)

    def tests_update_args_invalid_y(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.update(89, 1, 2, "invalid")

    def tests_update_args_y_negative(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.update(98, 1, 2, -4)

    def tests_update_args_size_before_x(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(89, "invalid", "invalid")

    def tests_update_args_size_before_y(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(89, "invalid", 2, "invalid")

    def tests_update_args_x_before_y(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class"""

    def tests_update_kwargs_1(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(sqr))

    def tests_update_kwargs_2(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(sqr))

    def tests_update_kwargs_3(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(sqr))

    def tests_update_kwargs_4(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(sqr))

    def tests_update_kwargs_width_setter(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(id=89, size=8)
        self.assertEqual(8, sqr.width)

    def tests_update_kwargs_height_setter(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(id=89, size=9)
        self.assertEqual(9, sqr.height)

    def tests_update_kwargs_None_id(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def tests_update_kwargs_None_id_and_more(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def tests_update_kwargs_twice(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(id=89, x=1)
        sqr.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(sqr))

    def tests_update_kwargs_invalid_size(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(size="invalid")

    def tests_update_kwargs_size_zero(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(size=0)

    def tests_update_kwargs_size_negative(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(size=-3)

    def tests_update_kwargs_invalid_x(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(x="invalid")

    def tests_update_kwargs_x_negative(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.update(x=-5)

    def tests_update_kwargs_invalid_y(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.update(y="invalid")

    def tests_update_kwargs_y_negative(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.update(y=-5)

    def tests_update_args_and_kwargs(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sqr))

    def tests_update_kwargs_wrong_keys(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(sqr))

    def tests_update_kwargs_some_wrong_keys(self):
        sqr = Square(10, 10, 10, 10)
        sqr.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(sqr))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of Square class"""

    def tests_to_dictionary_output(self):
        sqr = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, sqr.to_dictionary())

    def tests_to_dictionary_no_object_changes(self):
        sz1 = Square(10, 2, 1, 2)
        sz2 = Square(1, 2, 10)
        sz2.update(**sz1.to_dictionary())
        self.assertNotEqual(sz1, sz2)

    def tests_to_dictionary_arg(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sqr.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
