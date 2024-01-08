#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - print info about python lists
 * @p: ptr to python object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *lp;
	int obsize, i;

	lp = (PyListObject *)p;
	obsize = lp->ob_base.ob_size;

	printf("[*] Size of the Python List = %d\n", obsize);
	printf("[*] Allocated = %ld\n", lp->allocated);
	for (i = 0; i < obsize; i++)
	{
		printf("Element %d: %s\n", i, lp->ob_item[i]->ob_type->tp_name);
	}
}
