#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string info
 *
 * @p: Python Object
 * Return: void
 */
void print_python_string(PyObject *p)
{

    PyObject *p_repr, *l_str;

    (void)p_repr;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	p_repr = PyObject_Repr(p);
	l_str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(l_str));
}
