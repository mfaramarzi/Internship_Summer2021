#include <iostream>

// Function that, given a matrix of integers, builds a string with the entries of that matrix appended in clockwise order.
void BuildStringFromMatrix(int* Matrix, int NumRows, int NumColumns, char* OutBuffer)
{
	int topRow = 0, botRow = NumRows - 1, leftCol = 0, rightCol = NumColumns - 1;
	unsigned int index = 0;
	int n = 0;

	if (NumRows == 0 || NumColumns == 0)
	{
		OutBuffer[0] = '\0';
		return;
	}

	// Outter loop iterates through whole matrix - n is incremented inside loop	

	else
	{
		while (true)
		{
			// Move from left to right in a row of the matrix
			for (int col = leftCol; col <= rightCol; col++)
			{
				// current column + current row * numColumns treats 1d array like a 2d array
				int number = Matrix[col + topRow * NumColumns];
				if (number < 0)
				{
					number *= -1;
					OutBuffer[index++] = '-';
				}

				if (number < 10)
				{
					OutBuffer[index++] = number + 48;
				}
				else
				{
					int tempIntArr[10];
					unsigned int len = 0;
					for (; number > 0; number /= 10)
					{
						tempIntArr[len++] = number % 10;
					}

					for (int i = len - 1; i >= 0; i--)
					{
						OutBuffer[index++] = tempIntArr[i] + 48;
					}
				}
				//n++;
				if (++n == NumRows * NumColumns)
				{
					OutBuffer[index] = '\0';
					return;
				}
				OutBuffer[index++] = ',';
				OutBuffer[index++] = ' ';
			}
			// Move to next row
			topRow++;

			// Move from top to bottom of a column in matrix
			for (int row = topRow; row <= botRow; row++)
			{
				int number = Matrix[rightCol + row * NumColumns];

				if (number < 0)
				{
					number *= -1;
					OutBuffer[index++] = '-';
				}

				if (number < 10)
				{
					OutBuffer[index++] = number + 48;
				}
				else
				{
					int tempIntArr[10];
					unsigned int len = 0;
					for (; number > 0; number /= 10)
					{
						tempIntArr[len++] = number % 10;
					}

					for (int i = len - 1; i >= 0; i--)
					{
						OutBuffer[index++] = tempIntArr[i] + 48;
					}
				}
				//n++;
				if (++n == NumRows * NumColumns)
				{
					OutBuffer[index] = '\0';
					return;
				}
				OutBuffer[index++] = ',';
				OutBuffer[index++] = ' ';
			}
			// Decrement rightCol to move one column to the left
			rightCol--;

			// Move from rightmost column to leftmost column in a row of matrix
			for (int col = rightCol; col >= leftCol; col--)
			{
				int number = Matrix[col + botRow * NumColumns];

				if (number < 0)
				{
					number *= -1;
					OutBuffer[index++] = '-';
				}

				if (number < 10)
				{
					OutBuffer[index++] = number + 48;
				}
				else
				{
					int tempIntArr[10];
					unsigned int len = 0;
					for (; number > 0; number /= 10)
					{
						tempIntArr[len++] = number % 10;
					}

					for (int i = len - 1; i >= 0; i--)
					{
						OutBuffer[index++] = tempIntArr[i] + 48;
					}
				}

				//n++;
				if (++n == NumRows * NumColumns)
				{
					OutBuffer[index] = '\0';
					return;
				}
				OutBuffer[index++] = ',';
				OutBuffer[index++] = ' ';
			}
			// Decrement botRow to move "up" to next row of matrix
			botRow--;

			// Move from bottom of a column to top of column in a row of the matrix
			for (int row = botRow; row >= topRow; row--)
			{
				int number = Matrix[leftCol + row * NumColumns];

				if (number < 0)
				{
					number *= -1;
					OutBuffer[index++] = '-';
				}

				if (number < 10)
				{
					OutBuffer[index++] = number + 48;
				}
				else
				{
					int tempIntArr[10];
					unsigned int len = 0;
					for (; number > 0; number /= 10)
					{
						tempIntArr[len++] = number % 10;
					}

					for (int i = len - 1; i >= 0; i--)
					{
						OutBuffer[index++] = tempIntArr[i] + 48;
					}
				}

				//n++;
				if (++n == NumRows * NumColumns)
				{
					OutBuffer[index] = '\0';
					return;
				}
				OutBuffer[index++] = ',';
				OutBuffer[index++] = ' ';
			}
			// Increment to leftCol to move to next column to right
			leftCol++;
		}
	}




}


int main()
{

	int numRows, numCols;

	std::cin >> numRows >> numCols;
	int* matrix = nullptr;

	if (numRows == 0 || numCols == 0)
	{
		matrix = new int[1];
	}
	else
	{
		matrix = new int[numRows * numCols];
		for (int i = 0; i < numRows * numCols; i++)
		{
			std::cin >> matrix[i];
		}

	}

	char* outBuffer = new char[1000];

	BuildStringFromMatrix(matrix, numRows, numCols, outBuffer);

	std::cout << outBuffer << std::endl;
}
