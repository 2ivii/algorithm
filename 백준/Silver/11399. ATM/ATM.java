import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 사람 수 입력
        int n = sc.nextInt();
        int[] P = new int[n];

        // 인출 시간 입력
        for (int i = 0; i < n; i++) {
            P[i] = sc.nextInt();
        }

        // 버블 정렬을 이용해 오름차순 정렬 (기본적인 정렬 알고리즘 사용)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (P[j] > P[j + 1]) {
                    // 인접한 두 값을 교환
                    int temp = P[j];
                    P[j] = P[j + 1];
                    P[j + 1] = temp;
                }
            }
        }

        // 각 사람이 기다린 시간 계산
        int totalWaitTime = 0;
        int cumulativeTime = 0;

        for (int i = 0; i < n; i++) {
            cumulativeTime += P[i];  // 지금까지 걸린 시간
            totalWaitTime += cumulativeTime;  // 모든 사람의 대기 시간의 합
        }

        // 결과 출력
        System.out.println(totalWaitTime);

        sc.close();
    }
}
