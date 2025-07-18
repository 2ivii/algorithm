#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<long long> heights(N + 1); // 연병장 높이 배열
    vector<long long> diff(N + 2); // 차분 배열

    // 초기 높이 입력
    for (int i = 1; i <= N; ++i) {
        cin >> heights[i];
    }

    // 각 조교의 지시를 차분 배열에 반영
    for (int i = 0; i < M; ++i) {
        int a, b, k;
        cin >> a >> b >> k;

        diff[a] += k; // a번째 칸에 k 추가
        diff[b + 1] -= k; // b+1번째 칸에서 k 제거
    }

    // 차분 배열을 통해 최종 높이 계산
    long long current_addition = 0; // 현재 추가할 높이
    for (int i = 1; i <= N; ++i) {
        current_addition += diff[i]; // 현재까지의 높이 추가량
        heights[i] += current_addition; // 연병장 높이에 추가
    }

    // 결과 출력
    for (int i = 1; i <= N; ++i) {
        cout << heights[i] << " ";
    }
    cout << endl;

    return 0;
}
