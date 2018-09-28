#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r') as my_file:
    # This reads the metric file, just to make sure we're able to find it.
    print(my_file.read())
    # Write the kotlin file.

DATA = """
data class EnumerationMetricType(
    val userProperty: Boolean
) {
    fun setScalar(): Boolean = userProperty
}"""

with open("EnumerationMetricType.kt", 'w') as out_file:
    out_file.write(DATA)
