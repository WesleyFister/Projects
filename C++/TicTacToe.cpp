#include <iostream>
using namespace std;

int main();
void game_board(char game_move[3][3]);
void validation(int row, int column, int miniumum_number, int maximum_number, int player, char game_move[3][3]);

void game_board(char game_move[3][3])
{
    system("clear");
	cout << "          |          |" << endl;
	cout << "     " << game_move[0][0] << "    |     " << game_move[0][1] << "    |     " << game_move[0][2] << "     " << endl;
	cout << "          |          |" << endl;
	cout << "__________|__________|__________" << endl;
	cout << "          |          |" << endl;
	cout << "          |          |" << endl;
	cout << "     " << game_move[1][0] << "    |     " << game_move[1][1] << "    |     " << game_move[1][2] << "     " << endl;
	cout << "          |          |" << endl;
	cout << "__________|__________|__________" << endl;
	cout << "          |          |" << endl;
	cout << "          |          |" << endl;
	cout << "     " << game_move[2][0] << "    |     " << game_move[2][1] << "    |     " << game_move[2][2] << "     " << endl;
	cout << "          |          |" << endl;
}

char player1(char game_move[3][3])
{
    int row, column;
    cout << "Enter a row number Player 1 (1-3): ";
    cin >> row;
    row--;
    cout << "Enter a column number Player 1 (1-3): ";
    cin >> column;
    column--;
    validation(row, column, 0, 3, 1, game_move);
    
    if ((game_move[0][0] == 'X' and game_move[0][1] == 'X' and game_move[0][2] == 'X') or 
        (game_move[1][0] == 'X' and game_move[1][1] == 'X' and game_move[1][2] == 'X') or 
        (game_move[2][0] == 'X' and game_move[2][1] == 'X' and game_move[2][2] == 'X') or 
        (game_move[0][0] == 'X' and game_move[1][0] == 'X' and game_move[2][0] == 'X') or 
        (game_move[0][1] == 'X' and game_move[1][1] == 'X' and game_move[2][1] == 'X') or 
        (game_move[0][2] == 'X' and game_move[1][2] == 'X' and game_move[2][2] == 'X') or 
        (game_move[0][0] == 'X' and game_move[1][1] == 'X' and game_move[2][2] == 'X') or 
        (game_move[0][2] == 'X' and game_move[1][1] == 'X' and game_move[2][0] == 'X'))
    {
        game_board(game_move);
        cout << "Player 1 won!" << endl;
        exit(0);
    }

    return game_move[row][column];
}

char player2(char game_move[3][3])
{
    int row, column;
    cout << "Enter a row number Player 2 (1-3): ";
    cin >> row;
    row--;
    cout << "Enter a column number Player 2 (1-3): ";
    cin >> column;
    column--;
    validation(row, column, 0, 3, 2, game_move);

    if ((game_move[0][0] == 'O' and game_move[0][1] == 'O' and game_move[0][2] == 'O') or 
        (game_move[1][0] == 'O' and game_move[1][1] == 'O' and game_move[1][2] == 'O') or 
        (game_move[2][0] == 'O' and game_move[2][1] == 'O' and game_move[2][2] == 'O') or 
        (game_move[0][0] == 'O' and game_move[1][0] == 'O' and game_move[2][0] == 'O') or 
        (game_move[0][1] == 'O' and game_move[1][1] == 'O' and game_move[2][1] == 'O') or 
        (game_move[0][2] == 'O' and game_move[1][2] == 'O' and game_move[2][2] == 'O') or 
        (game_move[0][0] == 'O' and game_move[1][1] == 'O' and game_move[2][2] == 'O') or 
        (game_move[0][2] == 'O' and game_move[1][1] == 'O' and game_move[2][0] == 'O'))
    {
        game_board(game_move);
        cout << "Player 2 won!" << endl;
        exit(0);
    }

    return game_move[row][column];
}

void validation(int row, int column, int miniumum_number, int maximum_number, int player, char game_move[3][3])
{
    if (cin.fail() or (row < miniumum_number or row > maximum_number) or (column < miniumum_number or column > maximum_number) or (game_move[row][column] == 'X' or game_move[row][column] == 'O'))
    {
        cin.clear();
        cin.ignore();
        game_board(game_move);
        if (player == 1)
        {
            player1(game_move);
        }
        else
        {
            player2(game_move);
        }
    }
    else
    {
        if (player == 1)
        {
            game_move[row][column] = 'X';
        }
        else
        {
            game_move[row][column] = 'O';
        }
    }
}

int main()
{
    char game_move[3][3] = { {'*', '*', '*'}, {'*', '*', '*'}, {'*', '*', '*'} };
    
    while (game_move[0][0] == '*' or game_move[0][1] == '*' or game_move[0][2] == '*' or game_move[1][0] == '*' or game_move[1][1] == '*' or game_move[1][2] == '*' or game_move[2][0] == '*' or game_move[2][1] == '*' or game_move[2][2] == '*')
    {
        game_board(game_move);
        player1(game_move);

        if (game_move[0][0] == '*' or game_move[0][1] == '*' or game_move[0][2] == '*' or game_move[1][0] == '*' or game_move[1][1] == '*' or game_move[1][2] == '*' or game_move[2][0] == '*' or game_move[2][1] == '*' or game_move[2][2] == '*')
        {
            game_board(game_move);
            player2(game_move);
        }
        cout << "Nobody wins!" << endl;
    }

    return 0;
}
