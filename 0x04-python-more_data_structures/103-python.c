#include "Python.h"
#include <stdio.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - print info about python lists
 * @p: ptr to python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *lp;
	int listsize, i;
	const char *obtype;

	lp = (PyListObject *)p;
	if (lp && PyList_Check(lp))
	{
		listsize = lp->ob_base.ob_size;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %d\n", listsize);
		printf("[*] Allocated = %ld\n", lp->allocated);
		for (i = 0; i < listsize; i++)
		{
			obtype = lp->ob_item[i]->ob_type->tp_name;
			printf("Element %d: %s\n", i, obtype);
			if (strcmp(obtype, "bytes") == 0)
				print_python_bytes(lp->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes - print python bytes info
 * @p: ptr to a ptr object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbytes;
	int obsize, i;

	printf("[.] bytes object info\n");
	pbytes = (PyBytesObject *)p;

	if (!pbytes || !PyBytes_Check(pbytes))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
	}
	else
	{
		obsize = pbytes->ob_base.ob_size;
		printf("  size: %d\n", obsize);
		printf("  trying string: %s\n", pbytes->ob_sval);
		printf("  first %d bytes:", obsize < 10 ? obsize + 1 : 10);

		for (i = 0; i < obsize + 1 && i < 10; i++)
		{
			printf(" %02x", pbytes->ob_sval[i] & 0xff);
		}
		printf("\n");
	}
}
