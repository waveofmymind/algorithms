import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
    
    // 각 전화번호와 다음 전화번호를 비교해보며 접두어인지 확인합니다.
    for (int i = 0; i < phone_book.length - 1; i++) {
        if (phone_book[i+1].startsWith(phone_book[i])) {
            // 다음 전화번호가 현재 전화번호의 접두어인 경우 false를 반환합니다.
            return false;
        }
    }
    // 모든 전화번호를 비교한 후에도 접두어가 없는 경우 true를 반환합니다.
    return true;
    }
}