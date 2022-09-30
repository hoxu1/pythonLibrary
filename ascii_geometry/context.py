class ascii_context:
    """
    Instantiate ascii Geometry object.
    Different mathematical shapes can be drawn with a given symbol

    Parameters
    ----------
    symbol : char
        Symbol used for drawing.
    """

    def __init__(self, symbol):
        self.symbol = symbol

    def triangle(self, height):
        """
        Prints ascii tirangle.

        Parameters
        ----------
        height : int
            Height of the triangle.

        Returns
        -------
        void

        Examples
        --------
        >>> triangle(15)
                      #
                     ###
                    #####
                   #######
                  #########
                 ###########
                #############
               ###############
              #################
             ###################
            #####################
           #######################
          #########################
         ###########################
        #############################
        """
        for i in range(height):
            print((height - i - 1) * " " + (2*(i + 1) - 1) * "#" + (height - i - 1) * " ")
