#include <iostream>
#include <vector>
#include <set>

using Grid = std::vector<std::vector<char>>;
using BoolGrid = std::vector<std::vector<bool>>;
using Position = std::pair<int, int>;
using Group = std::set<Position>;

Grid getInput(unsigned int numRows, unsigned int numColumns);
void Gravity(Grid& grid);
Group GetGroup(int rowNum, int colNum, const Grid& grid, BoolGrid& visited);
void GetGroupHelper(int rowNum, int colNum, Group& group, const Grid& grid, BoolGrid& visited, bool& droppable);
bool IsInBounds(int rowPos, int colPos, const Grid& grid);

void DropGroup(const Group& group, Grid& grid);
void DropLetter(Grid& grid, int i, int j);

void PrintGrid(const Grid& grid);
void PrintBoolGrid(const BoolGrid& grid);
void PrintGroup(const Group& group);

int main()
{
	unsigned int numRows, numCols;

	while (std::cin >> numRows >> numCols)
	{
		if (numRows == 0 && numCols == 0)
		{
			return 0;
		}
		else
		{
			Grid grid = getInput(numRows, numCols);
			Gravity(grid);
		}
	}
}

Grid getInput(unsigned int numRows, unsigned int numColumns)
{
	Grid inputGrid(numRows);

	for (unsigned int i = 0; i < numRows; i++)
	{
		std::cin.ignore();
		inputGrid[i].reserve(numColumns);
		for (unsigned int j = 0; j < numColumns; j++)
		{
			inputGrid[i].push_back(std::cin.get());
		}
	}
	return inputGrid;
}

void Gravity(Grid& grid)
{
	bool finished{ false };

	while (!finished)
	{
		finished = true;
		for (int rowNum = grid.size() - 1; rowNum >= 0; rowNum--)
		{
			//std::cout << "rownum: " << rowNum << std::endl;
			BoolGrid visited(grid.size(), std::vector<bool>(grid[rowNum].size(), false));
			for (int colNum = 0; colNum < grid[rowNum].size(); colNum++)
			{	
				if (grid[rowNum][colNum] != ' ' && !visited[rowNum][colNum])
				{
					auto group = GetGroup(rowNum, colNum, grid, visited);
					//PrintGroup(group);
					//PrintGrid(grid);
					//PrintBoolGrid(visited);
					if (group.size() > 0)
					{
						DropGroup(group, grid);
						finished = false;
					}					
				}				
			}
		}
	}
	PrintGrid(grid);
}


// Recursively get connected positions
Group GetGroup(int rowNum, int colNum, const Grid& grid, BoolGrid& visited)
{
	Group group;
	bool droppable = true;

	GetGroupHelper(rowNum, colNum, group, grid, visited, droppable);

	if (!droppable)
		group.clear();
	return group;
}

void GetGroupHelper(int rowNum, int colNum, Group& group, const Grid& grid, BoolGrid& visited, bool& droppable)
{
	// out of bounds or space found
	if (!IsInBounds(rowNum, colNum, grid))
	{
		return;
	}

	if (grid[rowNum][colNum] == ' ')
	{
		visited[rowNum][colNum] = true;
		return;
	}

	// Group is supported - stop
	if (rowNum == grid.size() - 1)
	{
		droppable = false;
		visited[rowNum][colNum] = true;
		return;
	}

	// not visited, is letter, not supported
	if (!visited[rowNum][colNum])
	{
		group.emplace(rowNum, colNum);
		visited[rowNum][colNum] = true;
		GetGroupHelper(rowNum + 1, colNum, group, grid, visited, droppable);
		GetGroupHelper(rowNum - 1, colNum, group, grid, visited, droppable);
		GetGroupHelper(rowNum, colNum + 1, group, grid, visited, droppable);
		GetGroupHelper(rowNum, colNum - 1, group, grid, visited, droppable);
	}
	return;
}

bool IsInBounds(int rowPos, int colPos, const Grid& grid)
{
	return rowPos >= 0 && rowPos < grid.size() && colPos >= 0 && colPos < grid[0].size();
}

void DropLetter(Grid& grid, int i, int j)
{
	char temp = grid[i][j];
	grid[i][j] = grid[i + 1][j];
	grid[i + 1][j] = temp;
}

// Start at bottom of grid, work way up
void DropGroup(const Group& group, Grid& grid)
{
	
	for (auto reverseIterator = group.rbegin(); reverseIterator != group.rend(); ++reverseIterator)
	{
		DropLetter(grid, reverseIterator->first, reverseIterator->second);
	}
		
}

void PrintGrid(const Grid& grid)
{
	for (const auto& row : grid)
	{
		for (const auto& col : row)
		{
			//if (col == ' ')std::cout << "-";
			//else
			std::cout << col;
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
}

void PrintBoolGrid(const BoolGrid& grid)
{
	for (const auto& row : grid)
	{
		for (const auto& col : row)
		{			
			std::cout << col;
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
}

void PrintGroup(const Group& group)
{
	for (const auto& pos : group)
	{
		std::cout << pos.first << ' ' << pos.second << std::endl;
	}
}
