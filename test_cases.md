## Review cases: conductor calculation

### Single-phase system:

```
- DT range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 1, DT = 111 m.

- fp range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 0.6, DT = 10 m.
- fp range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 1.1, DT = 10 m.
- fp range satisfied (OK)                 -> V = 208 V, P = 300 W, fp = 0.8, DT = 10 m.

- I_load > 195 A (error)                  -> V = 208 V, P = 23500 W, fp = 1,   DT = 10 m.
- I_load < 195 A (OK)                     -> V = 208 V, P = 23400 W, fp = 1,   DT = 10 m.

- No conductor satisfies CT (error)       -> V = 208 V, P = 20000 W, fp = 1,   DT = 110 m.
- CT satisfied (OK)                       -> V = 208 V, P = 15000 W, fp = 1,   DT = 55 m.

- 214 V voltage case (OK)                 -> V = 214 V, P = 15000 W, fp = 0.8, DT = 10 m.
- 220 V voltage case (OK)                 -> V = 220 V, P = 15000 W, fp = 0.8, DT = 10 m.
```

### Two-phase system:

```
- DT range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 1, DT = 111 m.

- fp range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 0.6, DT = 10 m.
- fp range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 1.1, DT = 10 m.
- fp range satisfied (OK)                 -> V = 208 V, P = 300 W, fp = 0.8, DT = 10 m.

- I_load > 195 A (error)                  -> V = 208 V, P = 41000 W, fp = 1,   DT = 10 m.
- I_load < 195 A (OK)                     -> V = 208 V, P = 40000 W, fp = 1,   DT = 10 m.

- No conductor satisfies CT (error)       -> V = 208 V, P = 40000 W, fp = 1,   DT = 110 m.
- CT satisfied (OK)                       -> V = 208 V, P = 15000 W, fp = 1,   DT = 55 m.

- 214 V voltage case (OK)                 -> V = 214 V, P = 15000 W, fp = 0.8, DT = 10 m.
- 220 V voltage case (OK)                 -> V = 220 V, P = 15000 W, fp = 0.8, DT = 10 m.
```

### Three-phase system:

```
- DT range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 1, DT = 111 m.

- fp range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 0.6, DT = 10 m.
- fp range not satisfied (error)          -> V = 208 V, P = 300 W, fp = 1.1, DT = 10 m.
- fp range satisfied (OK)                 -> V = 208 V, P = 300 W, fp = 0.8, DT = 10 m.

- I_load > 195 A (error)                  -> V = 208 V, P = 71000 W, fp = 1,   DT = 10 m.
- I_load < 195 A (OK)                     -> V = 208 V, P = 70000 W, fp = 1,   DT = 10 m.

- No conductor satisfies CT (error)       -> V = 208 V, P = 70000 W, fp = 1,   DT = 110 m.
- CT satisfied (OK)                       -> V = 208 V, P = 50000 W, fp = 1,   DT = 55 m.

- 214 V voltage case (OK)                 -> V = 214 V, P = 30000 W, fp = 0.8, DT = 10 m.
- 220 V voltage case (OK)                 -> V = 220 V, P = 30000 W, fp = 0.8, DT = 10 m.
```
