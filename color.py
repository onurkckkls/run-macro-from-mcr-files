class Color:
    @staticmethod
    def rgb2hex(rgb1, rgb2=False, rgb3=False):
        """ From rgb values to HEX code 

        Args:
            rgb1 (int | tuple): values of rgb red value, or tuple of three rgb in tuple
            rgb2 (int, optional): Value of rgb green value, if first variable is tuple, it is optional. Defaults to False.
            rgb3 (int, optional): Value of rgb blue value, if first variable is tuple, it is optional. Defaults to False.

        Returns:
            str: HEX code of RGB values
        """
        if type(rgb1) is tuple:
            rgb1, rgb2, rgb3 = rgb1

        return "#{:02x}{:02x}{:02x}".format(rgb1, rgb2, rgb3)

    @staticmethod
    def hex2rgb(hexcode):
        """ From HEX code to rgb values

        Args:
            hexcode (str): string HEX code

        Returns:
            tuple: tuple of rgb values
        """
        return tuple(map(ord, hexcode[1:].decode("hex")))
