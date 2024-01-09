#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - print info about python lists
 * @p: ptr to python object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *lp;
	int i;

	lp = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", lp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", lp->allocated);
	for (i = 0; i < (int)lp->ob_base.ob_size; i++)
	{
		printf("Element\n");
	}
}
