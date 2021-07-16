
class TimeMap {

    /** Initialize your data structure here. */
    var map = [Int:[String:String]]() //timestamp, key, value
    var timestampsKeySorted = [String:Bool]()
    var keyToTimestamps = [String:[Int]]()
    
    init() {
    }
    
    func set(_ key: String, _ value: String, _ timestamp: Int) {
        map[timestamp] = [key:value]
        if keyToTimestamps[key] == nil {
            keyToTimestamps[key] = [Int]()
        }
        keyToTimestamps[key]?.append(timestamp)
        timestampsKeySorted[key] = false
    }
    func binarySearch(target: Int, source: [Int]) -> Int? {
        var low = source.startIndex
        var high = source.endIndex
        if source[low] == target || source[high - 1] == target {
            return target
        }
        
        while low != high {
            let mid = source.index(low, offsetBy: source.distance(from: low, to: high)/2)
            let midValue = source[mid]
            if midValue == target {
                return target
            } else if midValue > target {
                high = mid
            } else {
                low = source.index(after: mid)
            }
        }
        if low == 0 {
            return nil
        }
        return source[low-1]
    }
    func getSortedTimestamps(key:String) -> [Int]? {
        var timestamps = keyToTimestamps[key]
        if timestampsKeySorted[key] == false {
            timestamps?.sort(by: <)
            timestampsKeySorted[key] = true
        }
        return timestamps
    }
    func get(_ key: String, _ timestamp: Int) -> String {
        guard let sortedTimestamps = getSortedTimestamps(key: key) else {
            return ""
        }
        guard let targetTimestamp = binarySearch(target: timestamp, source: sortedTimestamps) else {
            return ""
        }
        return map[targetTimestamp]?[key] ?? ""
    }
}

let timeMap = TimeMap();
//timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
//timeMap.get("foo", 1);         // return "bar"
//timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
//timeMap.set("foo", "bar2", 4); // store the key "foo" and value "ba2r" along with timestamp = 4.
//timeMap.get("foo", 4);         // return "bar2"
//timeMap.get("foo", 5);         // return "bar2"

//timeMap.set("love", "high", 10)
//timeMap.set("love", "low", 20)
//timeMap.get("love", 5)

timeMap.set("ctnow", "ztpearaw", 1)
timeMap.set("a", "b", 2)
timeMap.set("gszaw", "ztpearaw", 3)
timeMap.set("ctnow", "gszaw", 4)
timeMap.get("gszaw", 5)

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap()
 * obj.set(key, value, timestamp)
 * let ret_2: String = obj.get(key, timestamp)
 */

/*
 ["TimeMap","set","set","get","get","get","get","get"]
 [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
 */
/*
                1   2   3       4     5
 ["TimeMap","set","set","set","set","get","get","get","get","get","get","set","get","get","get","set","set","set","set","get","get"]
 [[],["ctondw","ztpearaw",1],["vrobykydll","hwliiq",2],["gszaw","ztpearaw",3],["ctondw","gszaw",4],["gszaw",5],["ctondw",6],["ctondw",7],["gszaw",8],["vrobykydll",9],["ctondw",10],["vrobykydll","kcvcjzzwx",11],["vrobykydll",12],["ctondw",13],["vrobykydll",14],["ztpearaw","zondoubtib",15],["kcvcjzzwx","hwliiq",16],["wtgbfvg","vrobykydll",17],["hwliiq","gzsiivks",18],["kcvcjzzwx",19],["ztpearaw",20]]
 ans:
 [null,null,null,null,null,"ztpearaw","gszaw","gszaw","ztpearaw","hwliiq","gszaw",null,"kcvcjzzwx","gszaw","kcvcjzzwx",null,null,null,null,"hwliiq","zondoubtib"]
 */
