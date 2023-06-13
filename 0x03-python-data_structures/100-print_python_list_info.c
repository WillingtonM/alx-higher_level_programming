#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p);
void print_item_info(PyObject *prmItem, int prmitem_index);

/**
 * print_python_list_info - prints informations about Python Lists
 * @p: Python object
 */
void print_python_list_info(PyObject *p)
{
    int item_index;
    int obj_allocated_nb = 0;
    PyObject *item;
    Py_ssize_t obj_list_size = 0;

    if (PyList_Check(p))
    {
        obj_list_size = PyList_Size(p);
        obj_allocated_nb = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %d\n", (int)obj_list_size);
        printf("[*] Allocated = %d\n", obj_allocated_nb);

        for (item_index = 0; item_index < obj_list_size; item_index++)
        {
            item = PyList_GetItem(p, item_index);
            print_item_info(item, item_index);
        }
    }
}

/**
 * print_item_info - prints information of items of a python list
 * @prmItem: item of python object
 * @prmitem_index: item index
 */
void print_item_info(PyObject *prmItem, int prmitem_index)
{
    char *item_name;
    item_name = (char *)Py_TYPE(prmItem)->tp_name;
    printf("Element %d: %s\n", prmitem_index, item_name);
}