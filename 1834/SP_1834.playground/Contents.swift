import Foundation
class Solution {
    struct TaskData: CustomStringConvertible {
        var index : Int
        var enqueueTime : Int
        var costTime : Int
        var description : String { "(\(index))\(enqueueTime)-\(costTime)" }
    }
    var tasksByProcessTime = [Int:[Int]]()
    func getOrder(_ tasks: [[Int]]) -> [Int] {
        var taskDatas = [TaskData]()
        var tasksByCostTime = [Int:[TaskData]]()
        var tasksByEnqueueTime = [Int:[TaskData]]()
        for (i,task) in tasks.enumerated() {
            let enqueueTime = task.first!
            let costTime = task.last!
            let taskData = TaskData.init(index: i, enqueueTime: enqueueTime, costTime: costTime)
            taskDatas.append(taskData)
            
            var leTasksByCostTime = tasksByCostTime[costTime] ?? [TaskData]()
            leTasksByCostTime.append(taskData)
            tasksByCostTime[costTime] = leTasksByCostTime
            
            var leTasksByEnqueueTime = tasksByEnqueueTime[enqueueTime] ?? [TaskData]()
            leTasksByEnqueueTime.append(taskData)
            tasksByEnqueueTime[enqueueTime] = leTasksByEnqueueTime
        }
//        print(tasksByCostTime)
        var sortedCostTime = tasksByCostTime.keys.sorted(by: <)
        var sortedEnqueueTime = tasksByEnqueueTime.keys.sorted(by: <)
        var currentTime = 0
        var result = [Int]()
        func getMinCostTask(currentTime : Int) -> TaskData? {
            for costTime in sortedCostTime {
                if let tasks = tasksByCostTime[costTime] {
                    if let task = tasks.first(where: { (task) -> Bool in
                        task.enqueueTime <= currentTime
                    }) {
                        return task
                    }
                }
            }
            return nil
        }
        for i in 0..<tasks.count {
            let minEnqueueTime = sortedEnqueueTime.first ?? 0
            if currentTime < minEnqueueTime {
                currentTime = minEnqueueTime
            }
            print("current time:\t \(currentTime)")
            if let task = getMinCostTask(currentTime: currentTime) {
                print("append task:\t \(task)")
                result.append(task.index)
                tasksByCostTime[task.costTime]?.removeAll(where: { (aTask) -> Bool in
                    aTask.index == task.index
                })
                if tasksByCostTime[task.costTime]?.isEmpty == true {
                    tasksByCostTime.removeValue(forKey: task.costTime)
                    sortedCostTime.removeAll { (costTime) -> Bool in
                        task.costTime == costTime
                    }
                }
                currentTime += task.costTime
            }
            
        }
        return result
    }
}
//Solution().getOrder([[1,2],[2,4],[3,2],[4,1]])
//Solution().getOrder([[1,2],[2,4],[3,2],[4,1],[5,2]])
//Solution().getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]])

let result = Solution().getOrder([[46,9],[46,42],[30,46],[30,13],[30,24],[30,5],[30,21],[29,46],[29,41],[29,18],[29,16],[29,17],[29,5],[22,15],[22,13],[22,25],[22,49],[22,44]])
print(Date())
print(result)
print(Date())
