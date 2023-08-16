#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;

const int inf = 1e3;

#define AI_MARKER 'O'
#define PLAYER_MARKER 'X'
#define EMPTY_SPACE '-'

#define START_DEPTH 0

char board[3][3] = {{EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE},
                    {EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE},
                    {EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE}};

bool is_won(char board[3][3], char player)
{
    // Check rows
    for (int row = 0; row < 3; ++row)
    {
        if (board[row][0] == player && board[row][1] == player && board[row][2] == player)
            return true;
    }

    // Check columns
    for (int col = 0; col < 3; ++col)
    {
        if (board[0][col] == player && board[1][col] == player && board[2][col] == player)
            return true;
    }

    // Check diagonals
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
        return true;

    if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
        return true;

    return false;
}

void print_board(char board[3][3])
{
    cout << endl;
    cout << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << endl;
    cout << "--+---+--" << endl;
    cout << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << endl;
    cout << "--+---+--" << endl;
    cout << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << endl
         << endl;
}

bool is_valid_pos(int n)
{
    return (n >= 1 && n <= 9);
}

bool is_valid_move(char board[3][3], int x, int y)
{
    return board[x][y] == EMPTY_SPACE;
}

vector<pair<int, int>> get_legal_moves(char board[3][3])
{
    vector<pair<int, int>> legal_moves;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == EMPTY_SPACE)
            {
                legal_moves.push_back(make_pair(i, j));
            }
        }
    }

    return legal_moves;
}

bool board_is_full(char board[3][3])
{
    vector<pair<int, int>> legal_moves = get_legal_moves(board);

    if (legal_moves.size() == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// there is a problem there
bool is_draw(char board[3][3])
{
    bool ai_won = is_won(board, AI_MARKER);
    bool player_won = is_won(board, PLAYER_MARKER);

    if (!ai_won && !player_won && board_is_full(board))
    {
        return true;
    }

    return false;
}

pair<int, pair<int, int>> minimax_optimization(char board[3][3], char marker, int depth, int alpha, int beta)
{
    pair<int, int> best_move = make_pair(-1, -1);

    // AI is maximizer
    int best_score = (marker == AI_MARKER) ? -inf : inf;

    // If we hit a terminal state (leaf node), return the best score and move
    if (board_is_full(board) || is_won(board, AI_MARKER) || is_won(board, PLAYER_MARKER))
    {

        if (is_won(board, AI_MARKER))
        {
            return make_pair(inf, best_move);
        }
        else if (is_won(board, PLAYER_MARKER))
        {
            return make_pair(-inf, best_move);
        }
        else
        {
            return make_pair(0, best_move);
        }
    }

    vector<pair<int, int>> legal_moves = get_legal_moves(board);

    for (pair<int, int> curr_move : legal_moves)
    {
        board[curr_move.first][curr_move.second] = marker;

        // Maximizing player's turn
        if (marker == AI_MARKER)
        {
            int score = minimax_optimization(board, PLAYER_MARKER, depth + 1, alpha, beta).first;

            if (best_score < score)
            {
                best_score = score - depth * 10;
                best_move = curr_move;

                alpha = max(alpha, best_score);

                // Undo move
                board[curr_move.first][curr_move.second] = EMPTY_SPACE;

                // Apply alpha beta pruning
                if (beta <= alpha)
                {
                    break;
                }
            }
        }
        // Minimizing opponent's turn
        else
        {
            int score = minimax_optimization(board, AI_MARKER, depth + 1, alpha, beta).first;

            if (best_score > score)
            {
                best_score = score + depth * 10;
                best_move = curr_move;

                beta = min(beta, best_score);

                // Undo move
                board[curr_move.first][curr_move.second] = EMPTY_SPACE;

                // Apply alpha beta pruning
                if (beta <= alpha)
                {
                    break;
                }
            }
        }

        board[curr_move.first][curr_move.second] = EMPTY_SPACE; // Undo move
    }

    return make_pair(best_score, best_move);
}

void print_game_over()
{
    if (is_won(board, AI_MARKER))
    {
        cout << "AI WINS" << endl;
    }
    else if (is_won(board, PLAYER_MARKER))
    {
        cout << "YOU WINS" << endl;
    }
    else if (board_is_full(board))
    {
        cout << "GAME DRAW" << endl;
    }
}

bool is_game_over()
{
    if (board_is_full(board) || is_won(board, AI_MARKER) || is_won(board, PLAYER_MARKER))
        return true;
    return false;
}

void players_move()
{
    cout << "Your Move." << endl;
    while (true)
    {
        int row, col, n;
        cout << "Enter your position(1-9): ";
        cin >> n;

        if (!is_valid_pos(n))
        {
            cout << "Postion must be in range 1-9\n";
            continue;
        }

        n -= 1;

        row = n / 3;
        col = n % 3;

        if (!is_valid_move(board, row, col))
        {
            cout << "The position (" << row << ", " << col << ") is occupied. Try another one..." << endl;
            continue;
        }

        board[row][col] = PLAYER_MARKER;

        return;
    }
}

void ai_move()
{
    cout << "AI is moving..." << endl;

    // {score, move}
    pair<int, pair<int, int>> ai_move = minimax_optimization(board, AI_MARKER, START_DEPTH, -inf, inf);

    board[ai_move.second.first][ai_move.second.second] = AI_MARKER;

    sleep(1);
}

int main()
{

    cout << "\n********************************\n\n";
    cout << "\tTic Tac Toe AI\n\n";
    cout << "********************************\n\n";
    cout << "YOU = X\t\t\t AI = O\n\n";

    print_board(board);

    char current_player = PLAYER_MARKER;

    while (!is_game_over())
    {
        if (current_player == PLAYER_MARKER)
        {

            players_move();
        }
        else
        {

            ai_move();
        }

        current_player = current_player == PLAYER_MARKER ? AI_MARKER : PLAYER_MARKER;

        print_board(board);
    }

    cout << "********** GAME OVER **********\n\n";

    print_game_over();

    return 0;
}