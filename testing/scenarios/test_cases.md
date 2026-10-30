# Functional & Integration Test Scenarios

## 1. Functional Test Cases
| ID | Title | Input | Expected Output | Status |
|---|---|---|---|---|
| TC-01 | Temp Sensor Range | Value = 22.5°C | Item updates correctly, LastSeen timestamp refreshes | PASS |
| TC-02 | Edge Low Value | Temp = -40.0°C | System registers value, triggers Low-Temp Warning | PASS |
| TC-03 | Edge High Value | Temp = 85.0°C | Anomaly Rule triggers Critical Alert | PASS |
| TC-04 | Motion Integration | Motion = ON | Smart Light `IoT_Light_1` automatically switches ON | PASS |

## 2. Resilience & Recovery Simulation
- **Fault Scenario 1 (Network Disconnection):** Simulating device power failure. System detects offline status after 5 minutes and flags `IoT_Temp_1_Status = OFFLINE`.
- **Fault Scenario 2 (Corrupted Payload):** Sending string data to Number Item. System handles REST rejection gracefully without crashing rule engine.
