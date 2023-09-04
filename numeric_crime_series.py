'''
Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to crime. 

If you don't need to add specialized attributes or behavior, 
you can just use the original NumericSeries class directly. 
No subclassing required.

We get all of our parent's attributes and methods for free (no coding required).

This numbers add:

- a location attribute


'''

# From the name of the module (the file name without .py), import the class we want to inherit from
from numeric_series import NumericSeries

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


class NumericCrimeSeries(NumericSeries):
    """
    A class representing a numeric series customized for crime data.

    (Additional) Attributes:
       location (string): the location where the data was collected
    """

    def __init__(self, name, units, data, location):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            location (str): the location where the data was collected

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.location = location

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericCrimeSeries with name={self.name}, units={self.units}, location={self.location}, and {len(self.data)} data points: {self.data}"
        return str




if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "2015 to 2020 Crime"
    units1 = "Murder"
    data1 = [545, 407, 495, 215, 521]
    loc = "New York"

    object1 = NumericCrimeSeries(name1, units1, data1, loc)

  
    name2 = "2015 to 2020 Crime"
    units2 = "Robbery"
    data2 = [186, 225, 212, 196, 192, 189]
    loc2 = "New York"

    object2 = NumericCrimeSeries(name2, units2, data2, loc2)

    name3 = "2015 to 2020 Crime"
    units3 = "Felony Assault"
    data3 = [129, 125, 226, 156, 197, 86]
    loc3 = "New York"

    object3 = NumericCrimeSeries(name3, units3, data3, loc3)

    name4 = "2015 to 2020 Crime"
    units4 = "Burglary"
    data4 = [129, 141, 159, 243, 341]
    loc4 = "New York"

    object4 = NumericCrimeSeries(name4, units4, data4, loc4)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]


    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")