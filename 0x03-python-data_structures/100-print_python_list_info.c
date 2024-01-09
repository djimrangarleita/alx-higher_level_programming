#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - print info about python lists
 * @p: ptr to python object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *lp;
	long int listsize, i;

	lp = (PyListObject *)p;
	listsize = lp->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", listsize);
	printf("[*] Allocated = %ld\n", lp->allocated);
	for (i = 0; i < listsize; i++)
	{
		printf("Element %ld: %s\n", i, lp->ob_item[i]->ob_type->tp_name);
	}
}
