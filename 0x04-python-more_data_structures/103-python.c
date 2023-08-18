#include <Python.h>


void print_python_list_info(PyObject *listObject);
void print_python_bytes_info(PyObject *bytesObject);

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @listObject: A PyObject representing a list object.
 */
void print_python_list_info(PyObject *listObject)
{
	int listSize, allocatedSize, index;
	const char *elementType;
	PyListObject *list = (PyListObject *)listObject;
	PyVarObject *varObject = (PyVarObject *)listObject;

	listSize = varObject->ob_size;
	allocatedSize = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", listSize);
	printf("[*] Allocated = %d\n", allocatedSize);

	for (index = 0; index < listSize; index++)
	{
		elementType = list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, elementType);
		if (strcmp(elementType, "bytes") == 0)
			print_python_bytes_info(list->ob_item[index]);
	}
}

/**
 * print_python_bytes_info - Prints basic information on Python byte objects
 * @bytesObject: A PyObject representing a byte object.
 */
void print_python_bytes_info(PyObject *bytesObject)
{
	unsigned char byteIndex, displaySize;
	PyBytesObject *bytes = (PyBytesObject *)bytesObject;

	printf("[.] bytes object info\n");
	if (strcmp(bytesObject->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)bytesObject)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)bytesObject)->ob_size > 10)
		displaySize = 10;
	else
		displaySize = ((PyVarObject *)bytesObject)->ob_size + 1;

	printf("  first %d bytes: ", displaySize);
	for (byteIndex = 0; byteIndex < displaySize; byteIndex++)
	{
		printf("%02hhx", bytes->ob_sval[byteIndex]);
		if (byteIndex == (displaySize - 1))
			printf("\n");
		else
			printf(" ");
	}
}
