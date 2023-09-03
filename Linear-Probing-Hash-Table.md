## [Hash Table 구현] Linear Probing 방식의 Hash Table

### 접근

입력된 두 키가 서로 다르더라도, 해시의 결과로 결과값이 동일할 수 있다.

이를 **해시 충돌**이라고 한다.

그리고 이를 해결하기 위해 **Linear Probing**을 도입하면,

충돌이 발생할 경우 해당 위치에 한칸씩 더해서 저장한다. 

즉, table[index]가 null이 아닐때까지 index를 순차적으로 더해가면서, table[index] == null일때 값을 넣는다.



## LinearProbingHashTable 구현

``````kotlin
package com.example

class LinearProbingHashTable<K, V>(
    private val size: Int
) {
    private val table: Array<Pair<K, V>?> = arrayOfNulls(size)

    private fun hash(key: K): Int {
        return key.hashCode() % size
    }

    fun put(key: K, value: V) {
        var index = hash(key)
        while (table[index] != null) {
            if (table[index]!!.first == key) {
                table[index] = Pair(key, value)
                return
            }
            index = (index + 1) % size
        }
        table[index] = Pair(key, value)
    }

    fun remove(key: K) {
        var index = hash(key)

        while (table[index] != null) {
            if (table[index]!!.first == key) {
                table[index] = null
                return
            }
            index = (index + 1) % size
        }
    }

    fun get(key: K): V? {
        var index = hash(key)
        while (table[index] != null) {
            if (table[index]!!.first == key) {
                return table[index]!!.second
            }
            index = (index + 1) % size
        }
        return null
    }
}
``````

- **put**

​		table[index]가 null이면서, 해당 table[index]가 nulld 위치를 찾을때 까지 index 위치를 1씩 더해나간다.

​		특징은, table[index].first가 key와 동일하면, 이전의 key에 대해 수정을 요구하는 행위인 것이므로, 값을 갱신한다.

- **remove**

  마찬가지로 table[index].first == key 값을 찾으면, 해당 위치를 null로 변경하고 반환한다.

- **get**

  remove와 동일하게, key값에 대응하는 table[index]가 있으면 해당 값의 value를 반환한다.



