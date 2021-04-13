import xml.etree.ElementTree as ET
import datetime


def update_depart_and_return_fields(x=None, y=None):
    """
    Purpose: To update both the departure (x) and return (y) dates in test_payload1.xml
    :param x: The number of days to add to the current date to set the departure date.
    :type int
    :param y: The number of days to add to the current date to set the return date.
    :type int
    """

    tree = ET.parse('test_payload1.xml')
    root = tree.getroot()

    # Establish dates for calculation of delta
    today = datetime.date.today()

    # calculate the time delta for departure and return date
    depart_date = today + datetime.timedelta(x)
    return_date = today + datetime.timedelta(y)

    # apply the changes to the xml file
    root[0][2][0].text = depart_date.strftime("%Y%m%d")
    root[0][2][1].text = return_date.strftime("%Y%m%d")

    # save the changes
    tree.write('test_payload1.xml')


if __name__ == '__main__':
    update_depart_and_return_fields(3, 17)
