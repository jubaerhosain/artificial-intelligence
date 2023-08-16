#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;

const int inf = 1e3;

#define DRAW 0
#define PLAYER_WIN 1000
#define PLAYER_LOSS -1000

#define AI_MARKER 'O'
#define PLAYER_MARKER 'X'
#define EMPTY_SPACE '-'

#define START_DEPTH 0

// Print game state
void print_game_state(int state)
{
    if (PLAYER_WIN == state)
    {
        cout << "YOU WINS" << endl;
    }
    else if (DRAW == state)
    {
        cout << "GAME IS DRAW" << endl;
    }
    else if (PLAYER_LOSS == state)
    {
        cout << "AI WINS" << endl;
    }
}

// All possible player_winning states
vector<vector<pair<int, int>>> player_winning_states{
    // Every row
    {make_pair(0, 0), make_pair(0, 1), make_pair(0, 2)},
    {make_pair(1, 0), make_pair(1, 1), make_pair(1, 2)},
    {make_pair(2, 0), make_pair(2, 1), make_pair(2, 2)},

    // Every column
    {make_pair(0, 0), make_pair(1, 0), make_pair(2, 0)},
    {make_pair(0, 1), make_pair(1, 1), make_pair(2, 1)},
    {make_pair(0, 2), make_pair(1, 2), make_pair(2, 2)},

    // Every diagonal
    {make_pair(0, 0), make_pair(1, 1), make_pair(2, 2)},
    {make_pair(2, 0), make_pair(1, 1), make_pair(0, 2)}

};

// Print the current board state
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

// Get all available legal moves (spaces that are not occupied)
vector<pair<int, int>> get_legal_moves(char board[3][3])
{
    vector<pair<int, int>> legal_moves;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] != AI_MARKER && board[i][j] != PLAYER_MARKER)
            {
                legal_moves.push_back(make_pair(i, j));
            }
        }
    }

    return legal_moves;
}

// Check if a position is occupied
bool position_occupied(char board[3][3], pair<int, int> pos)
{
    vector<pair<int, int>> legal_moves = get_legal_moves(board);

    for (int i = 0; i < legal_moves.size(); i++)
    {
        if (pos.first == legal_moves[i].first && pos.second == legal_moves[i].second)
        {
            return false;
        }
    }

    return true;
}

// Get all board positions occupied by the given marker
vector<pair<int, int>> get_occupied_positions(char board[3][3], char marker)
{
    vector<pair<int, int>> occupied_positions;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (marker == board[i][j])
            {
                occupied_positions.push_back(make_pair(i, j));
            }
        }
    }

    return occupied_positions;
}

// Check if the board is full
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

// Check if the game has been won
bool game_is_won(vector<pair<int, int>> occupied_positions)
{
    bool game_won;

    for (int i = 0; i < player_winning_states.size(); i++)
    {
        game_won = true;
        vector<pair<int, int>> curr_player_win_state = player_winning_states[i];
        for (int j = 0; j < 3; j++)
        {
            if (!(find(begin(occupied_positions), end(occupied_positions), curr_player_win_state[j]) != end(occupied_positions)))
            {
                game_won = false;
                break;
            }
        }

        if (game_won)
        {
            break;
        }
    }
    return game_won;
}

char get_opponent_marker(char marker)
{
    char opponent_marker;
    if (marker == PLAYER_MARKER)
    {
        opponent_marker = AI_MARKER;
    }
    else
    {
        opponent_marker = PLAYER_MARKER;
    }

    return opponent_marker;
}

// Check if someone has won or lost
bool is_won(char board[3][3], char marker)
{
    vector<pair<int, int>> occupied_positions = get_occupied_positions(board, marker);
    bool won = game_is_won(occupied_positions);
    return won;
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

// Check if someone has won or lost
int get_board_state(char board[3][3], char marker)
{

    char opponent_marker = get_opponent_marker(marker);

    vector<pair<int, int>> occupied_positions = get_occupied_positions(board, marker);

    bool is_won = game_is_won(occupied_positions);

    if (is_won)
    {
        return PLAYER_WIN;
    }

    occupied_positions = get_occupied_positions(board, opponent_marker);
    bool is_lost = game_is_won(occupied_positions);

    if (is_lost)
    {
        return PLAYER_LOSS;
    }

    bool is_full = board_is_full(board);
    if (is_full)
    {
        return DRAW;
    }

    return DRAW;
}

// Apply the minimax game optimization algorithm for ai move
pair<int, pair<int, int>> minimax_optimization(char board[3][3], char marker, int depth, int alpha, int beta)
{
    // Initialize best move
    pair<int, int> best_move = make_pair(-1, -1);

    // AI is maximizer
    int best_score = (marker == AI_MARKER) ? -inf : inf;

    // If we hit a terminal state (leaf node), return the best score and move
    if (board_is_full(board) || !is_draw(board))
    {

        if (is_won(board, AI_MARKER))
        {
            return make_pair(inf, best_move);
        }
        else
        {
            return make_pair(-inf, best_move);
        }
    }

    // If we hit a terminal state (leaf node), return the best score and move
    // if (board_is_full(board) || DRAW != get_board_state(board, AI_MARKER))
    // {
    // 	best_score = get_board_state(board, AI_MARKER);
    // 	return std::make_pair(best_score, best_move);
    // }

    vector<pair<int, int>> legal_moves = get_legal_moves(board);

    for (pair<int, int> curr_move : legal_moves)
    {
        board[curr_move.first][curr_move.second] = marker;

        // Maximizing player's turn
        if (marker == AI_MARKER)
        {
            int score = minimax_optimization(board, PLAYER_MARKER, depth + 1, alpha, beta).first;

            // Get the best scoring move
            if (best_score < score)
            {
                best_score = score - depth * 10;
                best_move = curr_move;

                // Check if this branch's best move is worse than the best
                // option of a previously search branch. If it is, skip it
                alpha = max(alpha, best_score);
                board[curr_move.first][curr_move.second] = EMPTY_SPACE;
                if (beta <= alpha)
                {
                    break;
                }
            }

        } // Minimizing opponent's turn
        else
        {
            int score = minimax_optimization(board, AI_MARKER, depth + 1, alpha, beta).first;

            if (best_score > score)
            {
                best_score = score + depth * 10;
                best_move = curr_move;

                // Check if this branch's best move is worse than the best
                // option of a previously search branch. If it is, skip it
                beta = min(beta, best_score);
                board[curr_move.first][curr_move.second] = EMPTY_SPACE;
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

// Check if the game is finished
bool game_is_done(char board[3][3])
{
    if (board_is_full(board))
    {
        return true;
    }

    if (DRAW != get_board_state(board, AI_MARKER))
    {
        return true;
    }

    return false;
}

int main()
{
    char board[3][3] = {{EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE},
                        {EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE},
                        {EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE}};

    cout << "\n********************************\n\n";
    cout << "\tTic Tac Toe AI\n\n";
    cout << "********************************\n\n";
    cout << "YOU = X\t\t\t AI = O\n\n";

    print_board(board);

    while (!game_is_done(board))
    {
        int row, col, n;
        cout << "Enter your position(1-9): ";
        cin >> n;

        if (n < 1 || n > 9)
        {
            cout << "Postion must be in range 1-9\n";
            continue;
        }

        n -= 1;

        row = n / 3;
        col = n % 3;

        if (position_occupied(board, make_pair(row, col)))
        {
            cout << "The position (" << row << ", " << col << ") is occupied. Try another one..." << endl;
            continue;
        }
        else
        {
            board[row][col] = PLAYER_MARKER;
        }

        print_board(board);

        cout << "AI is moving...\n";
        sleep(1);

        // {score, move}
        pair<int, pair<int, int>> ai_move = minimax_optimization(board, AI_MARKER, START_DEPTH, -inf, inf);

        board[ai_move.second.first][ai_move.second.second] = AI_MARKER;

        print_board(board);
    }

    cout << "********** GAME OVER **********\n\n";

    int player_state = get_board_state(board, PLAYER_MARKER);
    print_game_state(player_state);

    return 0;
}