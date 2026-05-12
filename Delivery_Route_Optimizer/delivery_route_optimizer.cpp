#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

struct Edge {
    int u, v, weight;
};

struct Delivery {
    int from, to, profit;
    bool done = false;
};

// Convert index to place name
char getName(int i) {
    return 'A' + i;
}

// -------- Bellman-Ford --------
void bellmanFord(int V, int src, const vector<Edge>& edges, vector<int>& dist) {
    dist.assign(V, INT_MAX);
    dist[src] = 0;

    for (int i = 0; i < V - 1; i++) {
        for (const auto& e : edges) {
            if (dist[e.u] != INT_MAX && dist[e.u] + e.weight < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.weight;
            }
        }
    }
}

int main() {
    int V;
    cout << "Enter number of places: ";
    cin >> V;

    vector<Edge> edges;
    vector<Delivery> deliveries;

    int choice;

    do {
        cout << "\n====== DELIVERY OPTIMIZER ======\n";
        cout << "1. Add Road\n";
        cout << "2. Add Delivery\n";
        cout << "3. Show Data\n";
        cout << "4. Run Optimizer\n";
        cout << "5. Delete Road\n";
        cout << "6. Delete Delivery\n";
        cout << "7. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        // -------- ADD ROADS --------
        if (choice == 1) {
            while (true) {
                char u, v;
                int w;

                cout << "Enter (From To Distance) OR 0 to stop: ";
                cin >> u;
                if (u == '0') break;

                cin >> v >> w;

                edges.push_back({u - 'A', v - 'A', w});
                edges.push_back({v - 'A', u - 'A', w});

                cout << "Added: " << u << " <-> " << v << endl;
            }
        }

        // -------- ADD DELIVERY --------
        else if (choice == 2) {
            while (true) {
                char f, t;
                int p;

                cout << "Enter (From To Profit) OR 0 to stop: ";
                cin >> f;
                if (f == '0') break;

                cin >> t >> p;

                deliveries.push_back({f - 'A', t - 'A', p, false});

                cout << "Added: " << f << " -> " << t << endl;
            }
        }

        // -------- SHOW DATA --------
        else if (choice == 3) {
            cout << "\n--- Roads ---\n";
            for (size_t i = 0; i < edges.size(); i += 2) {
                cout << getName(edges[i].u)
                     << " <-> " << getName(edges[i].v)
                     << " | " << edges[i].weight << endl;
            }

            cout << "\n--- Deliveries ---\n";
            for (const auto& d : deliveries) {
                cout << getName(d.from)
                     << " -> " << getName(d.to)
                     << " | Profit: " << d.profit << endl;
            }
        }

        // -------- RUN OPTIMIZER --------
        else if (choice == 4) {
            char srcChar;
            cout << "Enter starting place: ";
            cin >> srcChar;

            int current = srcChar - 'A';

            int maxDeliveries, maxDistance;
            cout << "Enter max deliveries: ";
            cin >> maxDeliveries;

            cout << "Enter max distance: ";
            cin >> maxDistance;

            // Reset delivery status before each run
            for (auto &d : deliveries) d.done = false;

            // Sort deliveries by profit (descending)
            sort(deliveries.begin(), deliveries.end(),
                 [](const Delivery& a, const Delivery& b) {
                     return a.profit > b.profit;
                 });

            int totalProfit = 0, count = 0;

            cout << "\n======= FINAL PLAN =======\n";

            while (count < maxDeliveries) {
                vector<int> distFromCurrent;
                bellmanFord(V, current, edges, distFromCurrent);

                bool found = false;

                for (auto &d : deliveries) {
                    if (d.done) continue;

                    // Step 1: current -> pickup
                    if (distFromCurrent[d.from] == INT_MAX) continue;

                    // Step 2: pickup -> drop
                    vector<int> distFromPickup;
                    bellmanFord(V, d.from, edges, distFromPickup);

                    if (distFromPickup[d.to] == INT_MAX) continue;

                    int totalDist = distFromCurrent[d.from] + distFromPickup[d.to];

                    if (totalDist <= maxDistance) {
                        cout << "\nDelivery " << count + 1 << ":\n";
                        cout << "Route: " << getName(current)
                             << " -> " << getName(d.from)
                             << " -> " << getName(d.to) << endl;

                        cout << "Distance: " << totalDist << endl;
                        cout << "Profit: " << d.profit << endl;

                        totalProfit += d.profit;
                        count++;

                        current = d.to;
                        d.done = true;

                        found = true;
                        break;
                    }
                }

                if (!found) break;
            }

            cout << "\nTotal Deliveries Done: " << count << endl;
            cout << "Total Profit: " << totalProfit << endl;
        }

        // -------- DELETE ROAD --------
        else if (choice == 5) {
            char u, v;
            cout << "Enter road to delete: ";
            cin >> u >> v;

            int u_idx = u - 'A';
            int v_idx = v - 'A';

            edges.erase(
                remove_if(edges.begin(), edges.end(),
                    [&](const Edge& e) {
                        return (e.u == u_idx && e.v == v_idx) ||
                               (e.u == v_idx && e.v == u_idx);
                    }),
                edges.end()
            );

            cout << "Road deleted\n";
        }

        // -------- DELETE DELIVERY --------
        else if (choice == 6) {
            char f, t;
            cout << "Enter delivery to delete: ";
            cin >> f >> t;

            int f_idx = f - 'A';
            int t_idx = t - 'A';

            deliveries.erase(
                remove_if(deliveries.begin(), deliveries.end(),
                    [&](const Delivery& d) {
                        return d.from == f_idx && d.to == t_idx;
                    }),
                deliveries.end()
            );

            cout << "Delivery deleted\n";
        }

    } while (choice != 7);

    return 0;
}