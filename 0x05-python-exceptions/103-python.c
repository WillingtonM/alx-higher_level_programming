#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int sze, x, lmt;
	char *strng;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	sze = ((PyVarObject *)(p))->ob_size;
	strng = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", sze);
	printf("  trying string: %s\n", strng);

	if (sze >= 10)
		lmt = 10;
	else
		lmt = sze + 1;

	printf("  first %ld bytes:", lmt);

	for (x = 0; x < lmt; x++)
		if (strng[x] >= 0)
			printf(" %02x", strng[x]);
		else
			printf(" %02x", 256 + strng[x]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints list info
 *
 * @p: Python Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int sze, x;
	PyObject *objct;
	PyListObject *ls;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	sze = ((PyVarObject *)(p))->ob_size;
	ls = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", sze);
	printf("[*] Allocated = %ld\n", ls->allocated);

	for (x = 0; x < sze; x++)
	{
		objct = ls->ob_item[x];
		printf("Element %ld: %s\n", x, ((objct)->ob_type)->tp_name);

		if (PyBytes_Check(objct))
			print_python_bytes(objct);
		if (PyFloat_Check(objct))
			print_python_float(objct);
	}
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints float info
 *
 * @p: Python Object
 * Return: void
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *strng = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	strng = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", strng);
}
