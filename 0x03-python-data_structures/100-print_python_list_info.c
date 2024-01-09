#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - print info about python lists
 * @p: ptr to python object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *lp;

	lp = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", lp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", lp->allocated);
	printf("Element 0\n");
}
