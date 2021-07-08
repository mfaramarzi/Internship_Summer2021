#include <iostream>
#include <vector>
#include <set>

using Grid = std::vector<std::vector<char>>;
using BoolGrid = std::vector<std::vector<bool>>;
using Position = std::pair<int, int>;
using Group = std::set<Position>;

Grid getInput(unsigned int numRows, unsigned int numColumns);

void Gravity(Grid& grid);
std::set<Group> GetDroppableGroupsInRow(int rowNum, const Grid& grid, BoolGrid& visited);
Group GetGroup(int rowNum, int colNum, const Grid& grid, BoolGrid& visited);
void GetGroupHelper(int rowNum, int colNum, Group& group, const Grid& grid, BoolGrid& visited);

bool IsInBounds(int rowPos, int colPos, const Grid& grid);
bool IsGroupDroppable(const Group& group, const Grid& grid);

void DropGroup(const Group& group, Grid& grid);
void DropLetter(Grid& grid, int i, int j);

void PrintGrid(const Grid& grid);
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
	Grid inputGrid(numRows, std::vector<char>(numColumns));
	for (unsigned int i = 0; i < numRows; i++)
	{
		std::cin.ignore();
		for (unsigned int j = 0; j < numColumns; j++)
		{
			std::cin.get(inputGrid[i][j]);
		}
	}
	return inputGrid;
}

void Gravity(Grid& grid)
{
	// Start looping at end of grid and work back to beginning
	for (int i = grid.size() - 1; i >= 0; i--)
	{
		// For each row, create a new bool grid and collect all unsupported letters in grid
		BoolGrid visited(grid.size(), std::vector<bool>(grid[0].size(), false));
		std::set<Group> droppableGroups = GetDroppableGroupsInRow(i, grid, visited);

		int currentRow = i;

		// Drop the groups
		while (droppableGroups.size() > 0 && ++currentRow < grid.size())
		{
			for (const auto& group : droppableGroups)
			{
				DropGroup(group, grid);
			}
			// Shift down one row and attempt to drop again
			visited = BoolGrid(grid.size(), std::vector<bool>(grid[0].size(), false));
			droppableGroups = GetDroppableGroupsInRow(currentRow, grid, visited);
		}
	}
	PrintGrid(grid);
}

std::set<Group> GetDroppableGroupsInRow(int rowNum, const Grid& grid, BoolGrid& visited)
{
	std::set<Group> droppableGroups;

	for (int colNum = 0; colNum < grid[rowNum].size(); colNum++)
	{
		// If a character is found and it has not been visited
		if (grid[rowNum][colNum] != ' ' && !visited[rowNum][colNum])
		{
			// Recursively get all connected positions in the grid
			auto group = GetGroup(rowNum, colNum, grid, visited);
			// Check if the group is droppable
			if (group.size() > 0 && IsGroupDroppable(group, grid))
			{				
				droppableGroups.insert(std::move(group));
			}
		}
	}
	return droppableGroups;
}

// Recursively get connected positions
Group GetGroup(int rowNum, int colNum, const Grid& grid, BoolGrid& visited)
{
	Group group;
	GetGroupHelper(rowNum, colNum, group, grid, visited);
	return group;
}

void GetGroupHelper(int rowNum, int colNum, Group& group, const Grid& grid, BoolGrid& visited)
{
	if (!IsInBounds(rowNum, colNum, grid) || grid[rowNum][colNum] == ' ')
	{
		return;
	}
	else
	{
		if (!visited[rowNum][colNum])
		{
			group.insert({ rowNum, colNum });
			visited[rowNum][colNum] = true;
			GetGroupHelper(rowNum + 1, colNum, group, grid, visited);
			GetGroupHelper(rowNum - 1, colNum, group, grid, visited);
			GetGroupHelper(rowNum, colNum + 1, group, grid, visited);
			GetGroupHelper(rowNum, colNum - 1, group, grid, visited);
		}
	}
	return;
}

bool IsInBounds(int rowPos, int colPos, const Grid& grid)
{
	return rowPos >= 0 && rowPos < static_cast<int>(grid.size()) && colPos >= 0 && colPos < static_cast<int>(grid[0].size());
}

// Check if a group can be dropped
bool IsGroupDroppable(const Group& currentGroup, const Grid& grid)
{
	// Check if any letters are touching floor (set is sorted)
	auto highestRow = currentGroup.end();
	--highestRow;

	if (highestRow->first == grid.size() - 1)
	{
		return false;
	}

	return true;
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

