#include "Python.h"

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t i, py_list_size;
    PyObject *item;
    const char *item_type;

    list_object_cast = (PyListObject *)p;
    long int size = PyList_Size(p);
    py_list_size = PyList_Size(p);

    printf("[*] Size of the Python List = %d\n", (int)py_list_size);
    printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
    for (i = 0; i < py_list_size; i++)
    {
        item = PyList_GetItem(p, i);
        item_type = Py_TYPE(item)->tp_name;
        printf("Element %d: %s\n", (int)i, item_type);
    }

    for (index = 0; index < size; index++)
        printf("Element %i: %s\n", index, Py_TYPE(obj->ob_item[index])->tp_name);
}