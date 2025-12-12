#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

vector<string> load() {
    vector<string> tasks;
    ifstream file("tasks.txt");
    string line;
    while (getline(file, line)) {
        tasks.push_back(line);
    }
    return tasks;
}

void save(const vector<string>& tasks) {
    ofstream file("tasks.txt");
    for (auto &t : tasks) file << t << endl;
}

int main() {
    vector<string> tasks = load();
    int choice;
    string task;

    while (true) {
        cout << "\n1. Add task\n2. Show tasks\n3. Exit\nChoice: ";
        cin >> choice;
        cin.ignore();

        if (choice == 1) {
            cout << "Enter task: ";
            getline(cin, task);
            tasks.push_back(task);
            save(tasks);
        } 
        else if (choice == 2) {
            cout << "Your tasks:\n";
            for (auto &t : tasks) cout << "- " << t << endl;
        }
        else if (choice == 3) {
            break;
        }
        else {
            cout << "Error!\n";
        }
    }

    return 0;
}