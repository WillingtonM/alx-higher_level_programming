#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
    int i;
    long int ls_size = PyList_Size(p);
    PyListObject *list = (PyListObject *)p;
    const char *type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", ls_size);
    printf("[*] Allocated = %li\n", list->allocated);
    for (i = 0; i < ls_size; i++)
    {
        type = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, type);
        if (!strcmp(type, "bytes"))
            print_python_bytes(list->ob_item[i]);
    }
}

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    int i;
    long int ls_size;
    char *string = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &string, &ls_size);

    printf("  size: %li\n", ls_size);
    printf("  trying string: %s\n", string);
    if (ls_size < 10)
        printf("  first %li bytes:", ls_size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= ls_size && i < 10; i++)
        printf(" %02hhx", string[i]);
    printf("\n");
}