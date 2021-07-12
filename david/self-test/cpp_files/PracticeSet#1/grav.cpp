#include <iostream>
#include <vector>
#include <set>
// check if single cell not supported
// if group of cells not supported
    // drop each cell starting with bopttom row first until one is stuck

using GridType = std::vector<std::vector<char>>;
using Group = std::vector<std::pair<int, int>>;
using Pair = std::pair<int, int>;


GridType GetInput(int numRows, int numCols)
{

    GridType grid(numRows, std::vector<char>(numCols));
    for (int i = 0; i < numRows; i++)
    {
        std::cin.ignore();
        for (int j = 0; j < numCols; j++)
        {
            std::cin.get(grid[i][j]);
        }
    }   

    return grid;
}

bool isIsolated(std::pair<int, int> pos, const GridType& grid)
{
    // std::cout<<"iso\n";

    if (pos.first > 0)
    {
        if (grid[pos.first - 1][pos.second] != ' ')
        {
            return false;
        }
    }
    if (pos.first < static_cast<int>(grid.size()) - 1)
    {
        if (grid[pos.first + 1][pos.second] != ' ')
        {
            return false;
        }
    }
    if (pos.second > 0)
    {
        if (grid[pos.first][pos.second - 1] != ' ')
        {
            return false;
        }
    }
    if (pos.second < static_cast<int>(grid.size()))
    {
        if (grid[pos.first][pos.second + 1] != ' ')
        {
            return false;
        }
    }
    return true;

}

bool IsInBounds(int rowPos, int colPos, const GridType& grid)
{
    //  std::cout<<"inb\n";

    return rowPos >= 0 && rowPos < static_cast<int>(grid.size()) && colPos >= 0 && colPos < static_cast<int>(grid[0].size());
}

// start at bottom right
// move up until != ' '
// starting cell - find any connected cells.  Move down until one cell is stuck



int GetHighestRow(Group& group)
{
    int highest = 0;

    for (const auto& pair : group)
    {
       // std::cout << pair.first <<" " <<pair.second<< std::endl;
        if (pair.first >= highest)
        {
            highest = pair.first;
        }
    }
    //std::cout << "highest " << highest << std::endl;
    return highest;
}

bool IsGroupDroppable(Group& currentGroup, const GridType& grid)
{
    int highestRow = GetHighestRow(currentGroup);

    if (highestRow == grid.size() - 1)
    {
        return false;
    }


    for (const auto& pos : currentGroup)
    {
        if (!IsInBounds(pos.first + 1, pos.second, grid))
        {

            //std::cout << "failed1\n";
            return false;
        }
        if (pos.first == grid.size() - 1)
        {
            return false;
        }

        if (pos.first == highestRow && grid[pos.first + 1][pos.second] != ' ')
        {
            //std::cout << "failed2 " << grid[pos.first+1][pos.second] << std::endl;

            return false;
        }

       // std::cout << "passed\n";
        //std::cout << pos.first << " " << pos.second << grid[pos.first][pos.second] << std::endl;
    }
   
    return true;
}

//Group GetIsolatedPairs(int rowNum, const GridType& grid)
//{
//    Group group;
//    for (int i = 0; i < grid[rowNum].size(); i ++)
//    {
//        if (isIsolated({ rowNum,i },grid))
//            group.push_back({rowNum, i});
//    }
//}


void GetGroupRecHelper(int rowNum, int colNum, Group& group, const GridType& grid)
{   
    if (!IsInBounds(rowNum, colNum, grid) || grid[rowNum][colNum] == ' ')
    {
        return;
    }
    else
    {
   
        bool found{ false };
        for (const auto& pos : group)
        {
            if (pos.first == rowNum && pos.second == colNum) found = true;
        }
    
        if (!found)
        {
            group.push_back({ rowNum, colNum });
            //if(IsInBounds(rowNum+1, colNum, grid))
            GetGroupRecHelper(rowNum + 1, colNum, group, grid);

            //if (IsInBounds(rowNum - 1, colNum, grid))
            GetGroupRecHelper(rowNum - 1, colNum, group, grid);

          //  if (IsInBounds(rowNum, colNum + 1, grid))
            GetGroupRecHelper(rowNum, colNum + 1, group, grid);

           // if (IsInBounds(rowNum, colNum -1, grid))
            GetGroupRecHelper(rowNum, colNum - 1, group, grid);       
        }        
    }
    return;    
}

Group GetGroupRec(int rowNum, int colNum, const GridType& grid)
{    
    Group group;
    GetGroupRecHelper(rowNum, colNum, group, grid);    

    return group;
}

void Print(const GridType& grid)
{
    for (const auto& row : grid)
    {
        for (const auto& col : row)
        {
            std::cout << col;
        }
        std::cout << std::endl;
    }
}

void Swap(GridType& grid, int i, int j)
{
    //std::cout << "Before " << grid[i][j] << std::endl; 
    char temp = grid[i][j];
    grid[i][j] = grid[i + 1][j];
    grid[i + 1][j] = temp;

    //Print(grid);

    if (grid[i][j] != ' ' && grid[i + 1][j] != ' ')
    {
        std::cout << "bad swap\n";
    }
   // Print(grid);
   // std::cout<< " after: " << grid[i][j] << std::endl;

}

void DropGroup(Group& group, GridType& grid)
{
  //  Print(grid);
    for (auto& pos : group)
    {             
        Swap(grid, pos.first, pos.second);      
        //pos = std::pair<int,int>{ pos.first + 1, pos.second };
    }
   // Print(grid);
}

void Gravity(GridType& grid)
{
    

    for (int i = grid.size() - 1; i >= 0; i--)
    {
        GridType gridCopy = grid;
        for (int j = 0; j < grid[i].size(); j++)
        {
            if (grid[i][j] != ' ')
            {
                Group group = GetGroupRec(i, j, grid);               
                int temp = i;

                while (IsGroupDroppable(group, gridCopy) && temp < grid.size())
                {                   
                    std::cout << "droppable\n";
                   
                    DropGroup(group, grid);
                    temp++;
                    group = GetGroupRec(temp, j, grid);
                    Print(grid);
                    
                }
            }
        }
    }

    for (const auto& row : grid)
    {
        for (const auto& col : row)
        {
            std::cout << col;
        }
        std::cout << std::endl;
    }
}

int main(int argc, char** argv)
{
    int numRows, numCols;

    while (true)
    {
        std::cin >> numRows >> numCols;
        if (numRows == 0 && numCols == 0)
        {
            //std::cout << std::endl;
            break;
        }
        else
        {
            GridType grid = GetInput(numRows, numCols);

            Gravity(grid);
        }
    }

}