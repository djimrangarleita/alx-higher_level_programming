#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - print info about python lists
 * @p: ptr to python object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *lp;

	lp = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", lp->allocated);
}
