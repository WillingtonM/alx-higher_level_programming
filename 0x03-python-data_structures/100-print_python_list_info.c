#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    long int p_size = PyList_p_size(p);
    int indx;
    PyListObject *obj = (PyListObject *)p;

    printf("[*] p_size of the Python List = %li\n", p_size);
    printf("[*] Allocated = %li\n", obj->allocated);
    for (indx = 0; indx < p_size; indx++)
        printf("Element %i: %s\n", indx, Py_TYPE(obj->ob_item[indx])->tp_name);
}
