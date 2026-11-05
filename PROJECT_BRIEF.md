# AeroTwin-X — Preliminary Project Brief

**Title:** Physics-Based Aerospace Thermal-Fluid Digital Twin with Dynamic State Estimation and Predictive Fault Monitoring  
**Track:** DeepTech & Scientific Computing  
**Project type:** Individual project; preliminary simulation prototype

## Problem statement
Aerospace propulsion and engine thermal-management systems operate under changing heat loads and coolant-flow conditions. Temperature and flow disturbances can create thermal stress and reduce component reliability. A purely threshold-based monitoring approach may identify a problem only after a temperature limit is approached. A compact physics-based dynamic model can provide a foundation for predicting thermal response, estimating internal states from sensor measurements and detecting abnormal operating conditions.

This project addresses the initial modelling stage of that problem through a simplified engine-wall/coolant subsystem. The intended users are engineers working on propulsion, thermal management, testing and condition monitoring.

## Proposed solution
AeroTwin-X begins with a two-node lumped thermal-fluid model derived from the First Law of Thermodynamics. One control volume represents a hot engine wall and the second represents a well-mixed coolant inventory. Coupled ordinary differential equations describe heat input, wall-to-coolant convection, coolant enthalpy flow and external heat loss. Python and SciPy are used to simulate transient temperature response under illustrative changes in engine heat input and coolant mass flow. A small dashboard allows nominal operating parameters to be varied.

The next development stages are synthetic sensor measurements, observability analysis, Kalman-filter-based state estimation and residual-based fault detection for conditions such as coolant-flow degradation and sensor bias.

## Initial mathematical model
`Cw dTw/dt = Qin - hA(Tw - Tc) - UAamb(Tw - Tamb)`

`Cc dTc/dt = mdot cp,c(Tin - Tc) + hA(Tw - Tc)`

Here `Tw` and `Tc` are wall and coolant temperatures; `Cw` and `Cc` are thermal capacitances; `Qin` is engine-side heat input; `hA` is wall-to-coolant thermal conductance; and `mdot cp,c` represents coolant enthalpy transport.

## Current prototype and planned outcome
The submitted prototype demonstrates numerical integration of the coupled energy balances, transient temperature plots and a parameter-adjustable dashboard. The extended individual project is planned for completion by the end of November or December 2026, with state estimation, fault scenarios, validation strategy and expanded documentation.

## Assumptions and limitations
The initial model uses lumped, spatially uniform temperatures, constant thermal properties, single-phase incompressible coolant, a perfectly mixed coolant control volume and an effective external heat-loss term. Parameters are illustrative. This is not a complete engine simulation and has not yet been validated against engine test data or an experimental rig. The model will be refined and validated before any predictive-performance claims are made.
