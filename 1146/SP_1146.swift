class SnapshotArray {
    let length : Int
    var storage = [Int:[Int:Int]]()
    var storageMap = [Int:Int]()
    var storage_map_key = -1
    var current_snap_id = 0
    var current_snap = [Int:Int]()
    
    var changed = false
    init(_ length: Int) {
        self.length = length
    }
    
    func set(_ index: Int, _ val: Int) {
        if changed == false {
            storage_map_key += 1
            changed = true
        }
        current_snap[index] = val
    }
    
    func snap() -> Int {
//        print("cur_snap:\(current_snap_id) map_key:\(storage_map_key)")
        storageMap[current_snap_id] = storage_map_key
        if changed {
            storage[storage_map_key] = current_snap
            changed = false
        }
        current_snap_id += 1
        return current_snap_id - 1
    }
    
    func get(_ index: Int, _ snap_id: Int) -> Int {
        let id_to_key = storageMap[snap_id] ?? 0
//        print("get storageKey:\(id_to_key)")
        return storage[id_to_key]?[index] ?? 0
    }
    func desc() {
        print("map")
        print(storageMap)
        print("storage")
        print(storage)
    }
}
