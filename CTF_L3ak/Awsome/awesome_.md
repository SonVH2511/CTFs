```C
// O[1] Decompilation of $func0, known as $func0
int $func0(int param0) {
  // local index=1
  int local1;
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;
  // local index=7
  int local7;
  // local index=8
  int local8;
  // local index=9
  int local9;
  // local index=10
  long local10;

  global0 = local8 = (global0 - 0x10);
  label$1: {
    label$2: {
      label$3: {
        label$4: {
          label$5: {
            label$6: {
              label$7: {
                if (((unsigned) param0 >= 0xf5)) {
                  {
                    if (((unsigned) param0 >= -0x10033)) break label$1;
                    local5 = (param0 = (param0 + 0xb) & -0x8);
                    if ((local9 = *((unsigned int *) 0x10047c) == 0x0)) break label$4;
                    local3 = (0x0 - local5);
                    if ((local1 = *((unsigned int *) ((local7 = label$9: {
                      if (((unsigned) local5 < 0x100)) break(0x0) label$9;
                      if (((unsigned) local5 > 0xffffff)) break(0x1f) label$9;
                      ((((local5 >>> (0x6 - param0 = __clz_i32((param0 >>> 0x8)))) & 0x1) - (param0 << 0x1)) + 0x3e);
                    } << 0x2) + 0x1002e0)) == 0x0)) {
                      {
                        param0 = 0x0;
                        break label$7;
                      };
                    };
                    param0 = 0x0;
                    local4 = (local5 << (local7 != 0x1f) ? (0x19 - (local7 >>> 0x1)) : 0x0);
                    while (1) {
                      label$12: {
                        if (((unsigned) local6 = (*((unsigned int *) local1 + 0x4) & -0x8) < local5)) break label$12;
                        if (((unsigned) local6 = (local6 - local5) >= local3)) break label$12;
                        local2 = local1;
                        if (local3 = local6) break label$12;
                        local3 = 0x0;
                        param0 = local1;
                        break label$6;
                      };
                      param0 = local6 ? (local6 != local1 = *((unsigned int *) ((local1 + ((local4 >>> 0x1d) & 0x4)) + 0x10))) ? local6 = *((unsigned int *) (local1 + 0x14)) : param0 : param0;
                      local4 = (local4 << 0x1);
                      if (local1) break label$11;
                    break ;
                    };
                    break label$7;
                  };
                };
                if ((local1 = (local2 = *((unsigned int *) 0x100478) >>> param0 = (local5 = ((unsigned) param0 < 0xb) ? 0x10 : ((param0 + 0xb) & -0x8) >>> 0x3)) & 0x3)) {
                  {
                    label$14: {
                      if ((local4 = (param0 = (local1 = (((local1 ^ -0x1) & 0x1) + param0) << 0x3) + 0x100370) != local3 = *((unsigned int *) param0 = *((unsigned int *) (param0 + 0x100378)) + 0x8))) {
                        {
                          *((unsigned int *) local3 + 0xc) = local4;
                          *((unsigned int *) local4 + 0x8) = local3;
                          break label$14;
                        };
                      };
                      *((unsigned int *) 0x100478) = (local2 & __rotl_i32(-0x2, local1));
                    };
                    local3 = (param0 + 0x8);
                    *((unsigned int *) param0 + 0x4) = (local1 = (local1 << 0x3) | 0x3);
                    *((unsigned int *) param0 = (param0 + local1) + 0x4) = (*((unsigned int *) param0 + 0x4) | 0x1);
                    break label$1;
                  };
                };
                if (((unsigned) local5 <= *((unsigned int *) 0x100480))) break label$4;
                label$16: {
                  label$17: {
                    if ((local1 == 0x0)) {
                      {
                        if ((param0 = *((unsigned int *) 0x10047c) == 0x0)) break label$4;
                        local3 = ((*((unsigned int *) local1 = *((unsigned int *) ((__ctz_i32(param0) << 0x2) + 0x1002e0)) + 0x4) & -0x8) - local5);
                        local2 = local1;
                        while (1) {
                          label$20: {
                            if (param0 = *((unsigned int *) local1 + 0x10)) break label$20;
                            if (param0 = *((unsigned int *) (local1 + 0x14))) break label$20;
                            local7 = *((unsigned int *) local2 + 0x18);
                            label$21: {
                              label$22: {
                                if ((local2 == param0 = *((unsigned int *) local2 + 0xc))) {
                                  {
                                    if (local1 = *((unsigned int *) (local2 + local4 = *((unsigned int *) param0 = (local2 + 0x14)) ? 0x14 : 0x10))) break label$22;
                                    param0 = 0x0;
                                    break label$21;
                                  };
                                };
                                *((unsigned int *) local1 = *((unsigned int *) local2 + 0x8) + 0xc) = param0;
                                *((unsigned int *) param0 + 0x8) = local1;
                                break label$21;
                              };
                              local4 = local4 ? param0 : (local2 + 0x10);
                              while (1) {
                                local6 = local4;
                                local4 = local1 = *((unsigned int *) local1) ? local1 = (param0 = local1 + 0x14) : (param0 + 0x10);
                                if (local1 = *((unsigned int *) (param0 + local1 ? 0x14 : 0x10))) break label$24;
                              break ;
                              };
                              *((unsigned int *) local6) = 0x0;
                            };
                            if ((local7 == 0x0)) break label$16;
                            if ((local2 != *((unsigned int *) local1 = ((*((unsigned int *) local2 + 0x1c) << 0x2) + 0x1002e0)))) {
                              {
                                *((unsigned int *) (local7 + (*((unsigned int *) local7 + 0x10) == local2) ? 0x10 : 0x14)) = param0;
                                if ((param0 == 0x0)) break label$16;
                                break label$17;
                              };
                            };
                            *((unsigned int *) local1) = param0;
                            if (param0) break label$17;
                            *((unsigned int *) 0x10047c) = (*((unsigned int *) 0x10047c) & __rotl_i32(-0x2, *((unsigned int *) local2 + 0x1c)));
                            break label$16;
                          };
                          local3 = local1 = ((unsigned) local1 < local3) ? local1 = ((*((unsigned int *) param0 + 0x4) & -0x8) - local5) : local3;
                          local2 = local1 ? param0 : local2;
                          local1 = param0;
                          break label$19;
                        break ;
                        };
                      };
                    };
                    label$26: {
                      if ((local4 = (param0 = (local1 = __ctz_i32(((local4 = (0x2 << param0) | (0x0 - local4)) & (local1 << param0))) << 0x3) + 0x100370) != local3 = *((unsigned int *) param0 = *((unsigned int *) (param0 + 0x100378)) + 0x8))) {
                        {
                          *((unsigned int *) local3 + 0xc) = local4;
                          *((unsigned int *) local4 + 0x8) = local3;
                          break label$26;
                        };
                      };
                      *((unsigned int *) 0x100478) = (local2 & __rotl_i32(-0x2, local1));
                    };
                    *((unsigned int *) param0 + 0x4) = (local5 | 0x3);
                    *((unsigned int *) local6 = (param0 + local5) + 0x4) = (local4 = (local1 = (local1 << 0x3) - local5) | 0x1);
                    *((unsigned int *) (param0 + local1)) = local4;
                    if (local3 = *((unsigned int *) 0x100480)) {
                      {
                        local1 = ((local3 & -0x8) + 0x100370);
                        local2 = *((unsigned int *) 0x100488);
                        local3 = label$29: {
                          if (((local5 = *((unsigned int *) 0x100478) & local3 = (0x1 << (local3 >>> 0x3))) == 0x0)) {
                            {
                              *((unsigned int *) 0x100478) = (local3 | local5);
                              break(local1) label$29;
                            };
                          };
                          *((unsigned int *) local1 + 0x8);
                        };
                        *((unsigned int *) local1 + 0x8) = local2;
                        *((unsigned int *) local3 + 0xc) = local2;
                        *((unsigned int *) local2 + 0xc) = local1;
                        *((unsigned int *) local2 + 0x8) = local3;
                      };
                    };
                    local3 = (param0 + 0x8);
                    *((unsigned int *) 0x100488) = local6;
                    *((unsigned int *) 0x100480) = local4;
                    break label$1;
                  };
                  *((unsigned int *) param0 + 0x18) = local7;
                  if (local1 = *((unsigned int *) local2 + 0x10)) {
                    {
                      *((unsigned int *) param0 + 0x10) = local1;
                      *((unsigned int *) local1 + 0x18) = param0;
                    };
                  };
                  if ((local1 = *((unsigned int *) (local2 + 0x14)) == 0x0)) break label$16;
                  *((unsigned int *) (param0 + 0x14)) = local1;
                  *((unsigned int *) local1 + 0x18) = param0;
                };
                label$32: {
                  label$33: {
                    if (((unsigned) local3 >= 0x10)) {
                      {
                        *((unsigned int *) local2 + 0x4) = (local5 | 0x3);
                        *((unsigned int *) local4 = (local2 + local5) + 0x4) = (local3 | 0x1);
                        *((unsigned int *) (local3 + local4)) = local3;
                        if ((local6 = *((unsigned int *) 0x100480) == 0x0)) break label$33;
                        param0 = ((local6 & -0x8) + 0x100370);
                        local1 = *((unsigned int *) 0x100488);
                        local6 = label$35: {
                          if (((local5 = *((unsigned int *) 0x100478) & local6 = (0x1 << (local6 >>> 0x3))) == 0x0)) {
                            {
                              *((unsigned int *) 0x100478) = (local5 | local6);
                              break(param0) label$35;
                            };
                          };
                          *((unsigned int *) param0 + 0x8);
                        };
                        *((unsigned int *) param0 + 0x8) = local1;
                        *((unsigned int *) local6 + 0xc) = local1;
                        *((unsigned int *) local1 + 0xc) = param0;
                        *((unsigned int *) local1 + 0x8) = local6;
                        break label$33;
                      };
                    };
                    *((unsigned int *) local2 + 0x4) = (param0 = (local3 + local5) | 0x3);
                    *((unsigned int *) param0 = (param0 + local2) + 0x4) = (*((unsigned int *) param0 + 0x4) | 0x1);
                    break label$32;
                  };
                  *((unsigned int *) 0x100488) = local4;
                  *((unsigned int *) 0x100480) = local3;
                };
                local3 = (local2 + 0x8);
                break label$1;
              };
              if (((param0 | local2) == 0x0)) {
                {
                  local2 = 0x0;
                  if ((param0 = ((param0 = (0x2 << local7) | (0x0 - param0)) & local9) == 0x0)) break label$4;
                  param0 = *((unsigned int *) ((__ctz_i32(param0) << 0x2) + 0x1002e0));
                };
              };
              if ((param0 == 0x0)) break label$5;
            };
            while (1) {
              local9 = local7 = ((unsigned) local6 = (local4 = (*((unsigned int *) param0 + 0x4) & -0x8) - local5) < local3) ? param0 : local2;
              if ((local1 = *((unsigned int *) param0 + 0x10) == 0x0)) {
                local1 = *((unsigned int *) (param0 + 0x14));
              };
              local2 = param0 = ((unsigned) local4 < local5) ? local2 : local9;
              local3 = param0 ? local3 : local7 ? local6 : local3;
              if (param0 = local1) break label$38;
            break ;
            };
          };
          if ((local2 == 0x0)) break label$4;
          if ((((unsigned) local5 <= param0 = *((unsigned int *) 0x100480)) & ((unsigned) local3 >= (param0 - local5)))) break label$4;
          local7 = *((unsigned int *) local2 + 0x18);
          label$40: {
            label$41: {
              if ((local2 == param0 = *((unsigned int *) local2 + 0xc))) {
                {
                  if (local1 = *((unsigned int *) (local2 + local4 = *((unsigned int *) param0 = (local2 + 0x14)) ? 0x14 : 0x10))) break label$41;
                  param0 = 0x0;
                  break label$40;
                };
              };
              *((unsigned int *) local1 = *((unsigned int *) local2 + 0x8) + 0xc) = param0;
              *((unsigned int *) param0 + 0x8) = local1;
              break label$40;
            };
            local4 = local4 ? param0 : (local2 + 0x10);
            while (1) {
              local6 = local4;
              local4 = local1 = *((unsigned int *) local1) ? local1 = (param0 = local1 + 0x14) : (param0 + 0x10);
              if (local1 = *((unsigned int *) (param0 + local1 ? 0x14 : 0x10))) break label$43;
            break ;
            };
            *((unsigned int *) local6) = 0x0;
          };
          if ((local7 == 0x0)) break label$2;
          if ((local2 != *((unsigned int *) local1 = ((*((unsigned int *) local2 + 0x1c) << 0x2) + 0x1002e0)))) {
            {
              *((unsigned int *) (local7 + (*((unsigned int *) local7 + 0x10) == local2) ? 0x10 : 0x14)) = param0;
              if ((param0 == 0x0)) break label$2;
              break label$3;
            };
          };
          *((unsigned int *) local1) = param0;
          if (param0) break label$3;
          *((unsigned int *) 0x10047c) = (*((unsigned int *) 0x10047c) & __rotl_i32(-0x2, *((unsigned int *) local2 + 0x1c)));
          break label$2;
        };
        label$45: {
          label$46: {
            label$47: {
              label$48: {
                label$49: {
                  if (((unsigned) local5 > local1 = *((unsigned int *) 0x100480))) {
                    {
                      if (((unsigned) local5 >= param0 = *((unsigned int *) 0x100484))) {
                        {
                          param0 = __grow_memory_size((local2 = ((local5 + 0x1002f) & -0x10000) >>> 0x10));
                          *((unsigned int *) local1 = (local8 + 0x4) + 0x8) = 0x0;
                          *((unsigned int *) local1 + 0x4) = local2 = (param0 == -0x1) ? 0x0 : (local2 & -0x10000);
                          *((unsigned int *) local1) = local2 ? 0x0 : (param0 << 0x10);
                          if ((local1 = *((unsigned int *) local8 + 0x4) == 0x0)) {
                            {
                              local3 = 0x0;
                              break label$1;
                            };
                          };
                          local6 = *((unsigned int *) local8 + 0xc);
                          *((unsigned int *) 0x100490) = param0 = (local3 = *((unsigned int *) local8 + 0x8) + *((unsigned int *) 0x100490));
                          *((unsigned int *) 0x100494) = ((unsigned) param0 < local2) ? local2 = *((unsigned int *) 0x100494) : param0;
                          label$53: {
                            label$54: {
                              if (local2 = *((unsigned int *) 0x10048c)) {
                                {
                                  param0 = 0x100360;
                                  while (1) {
                                    if ((local1 == (local4 = *((unsigned int *) param0) + local7 = *((unsigned int *) param0 + 0x4)))) break label$54;
                                    if (param0 = *((unsigned int *) param0 + 0x8)) break label$56;
                                  break ;
                                  };
                                  break label$53;
                                };
                              };
                              if ((((unsigned) param0 <= local1) ? param0 = *((unsigned int *) 0x10049c) : 0x0 == 0x0)) {
                                *((unsigned int *) 0x10049c) = local1;
                              };
                              *((unsigned int *) 0x1004a0) = 0xfff;
                              *((unsigned int *) 0x10036c) = local6;
                              *((unsigned int *) 0x100364) = local3;
                              *((unsigned int *) 0x100360) = local1;
                              *((unsigned int *) 0x10037c) = 0x100370;
                              *((unsigned int *) 0x100384) = 0x100378;
                              *((unsigned int *) 0x100378) = 0x100370;
                              *((unsigned int *) 0x10038c) = 0x100380;
                              *((unsigned int *) 0x100380) = 0x100378;
                              *((unsigned int *) 0x100394) = 0x100388;
                              *((unsigned int *) 0x100388) = 0x100380;
                              *((unsigned int *) 0x10039c) = 0x100390;
                              *((unsigned int *) 0x100390) = 0x100388;
                              *((unsigned int *) 0x1003a4) = 0x100398;
                              *((unsigned int *) 0x100398) = 0x100390;
                              *((unsigned int *) 0x1003ac) = 0x1003a0;
                              *((unsigned int *) 0x1003a0) = 0x100398;
                              *((unsigned int *) 0x1003b4) = 0x1003a8;
                              *((unsigned int *) 0x1003a8) = 0x1003a0;
                              *((unsigned int *) 0x1003bc) = 0x1003b0;
                              *((unsigned int *) 0x1003b0) = 0x1003a8;
                              *((unsigned int *) 0x1003b8) = 0x1003b0;
                              *((unsigned int *) 0x1003c4) = 0x1003b8;
                              *((unsigned int *) 0x1003c0) = 0x1003b8;
                              *((unsigned int *) 0x1003cc) = 0x1003c0;
                              *((unsigned int *) 0x1003c8) = 0x1003c0;
                              *((unsigned int *) 0x1003d4) = 0x1003c8;
                              *((unsigned int *) 0x1003d0) = 0x1003c8;
                              *((unsigned int *) 0x1003dc) = 0x1003d0;
                              *((unsigned int *) 0x1003d8) = 0x1003d0;
                              *((unsigned int *) 0x1003e4) = 0x1003d8;
                              *((unsigned int *) 0x1003e0) = 0x1003d8;
                              *((unsigned int *) 0x1003ec) = 0x1003e0;
                              *((unsigned int *) 0x1003e8) = 0x1003e0;
                              *((unsigned int *) 0x1003f4) = 0x1003e8;
                              *((unsigned int *) 0x1003f0) = 0x1003e8;
                              *((unsigned int *) 0x1003fc) = 0x1003f0;
                              *((unsigned int *) 0x100404) = 0x1003f8;
                              *((unsigned int *) 0x1003f8) = 0x1003f0;
                              *((unsigned int *) 0x10040c) = 0x100400;
                              *((unsigned int *) 0x100400) = 0x1003f8;
                              *((unsigned int *) 0x100414) = 0x100408;
                              *((unsigned int *) 0x100408) = 0x100400;
                              *((unsigned int *) 0x10041c) = 0x100410;
                              *((unsigned int *) 0x100410) = 0x100408;
                              *((unsigned int *) 0x100424) = 0x100418;
                              *((unsigned int *) 0x100418) = 0x100410;
                              *((unsigned int *) 0x10042c) = 0x100420;
                              *((unsigned int *) 0x100420) = 0x100418;
                              *((unsigned int *) 0x100434) = 0x100428;
                              *((unsigned int *) 0x100428) = 0x100420;
                              *((unsigned int *) 0x10043c) = 0x100430;
                              *((unsigned int *) 0x100430) = 0x100428;
                              *((unsigned int *) 0x100444) = 0x100438;
                              *((unsigned int *) 0x100438) = 0x100430;
                              *((unsigned int *) 0x10044c) = 0x100440;
                              *((unsigned int *) 0x100440) = 0x100438;
                              *((unsigned int *) 0x100454) = 0x100448;
                              *((unsigned int *) 0x100448) = 0x100440;
                              *((unsigned int *) 0x10045c) = 0x100450;
                              *((unsigned int *) 0x100450) = 0x100448;
                              *((unsigned int *) 0x100464) = 0x100458;
                              *((unsigned int *) 0x100458) = 0x100450;
                              *((unsigned int *) 0x10046c) = 0x100460;
                              *((unsigned int *) 0x100460) = 0x100458;
                              *((unsigned int *) 0x100474) = 0x100468;
                              *((unsigned int *) 0x100468) = 0x100460;
                              *((unsigned int *) 0x10048c) = local2 = (param0 = ((local1 + 0xf) & -0x8) - 0x8);
                              *((unsigned int *) 0x100470) = 0x100468;
                              *((unsigned int *) 0x100484) = param0 = ((local4 = (local3 - 0x28) + (local1 - param0)) + 0x8);
                              *((unsigned int *) local2 + 0x4) = (param0 | 0x1);
                              *((unsigned int *) (local1 + local4) + 0x4) = 0x28;
                              *((unsigned int *) 0x100498) = 0x200000;
                              break label$45;
                            };
                            if ((((unsigned) local2 < local4) | ((unsigned) local1 <= local2))) break label$53;
                            if ((local4 = *((unsigned int *) param0 + 0xc) & 0x1)) break label$53;
                            if (((local4 >>> 0x1) == local6)) break label$49;
                          };
                          *((unsigned int *) 0x10049c) = ((unsigned) param0 < local1) ? param0 = *((unsigned int *) 0x10049c) : local1;
                          local4 = (local1 + local3);
                          param0 = 0x100360;
                          label$58: {
                            label$59: {
                              while (1) if ((local4 != *((unsigned int *) param0))) {
                                {
                                  if (param0 = *((unsigned int *) param0 + 0x8)) break label$60;
                                  break label$59;
                                };
                              };
                              if ((local7 = *((unsigned int *) param0 + 0xc) & 0x1)) break label$59;
                              if (((local7 >>> 0x1) == local6)) break label$58;
                            };
                            param0 = 0x100360;
                            while (1) label$63: {
                              if (((unsigned) local2 >= local4 = *((unsigned int *) param0))) {
                                if (((unsigned) local7 = (local4 + *((unsigned int *) param0 + 0x4)) > local2)) continue label$63;
                              };
                              param0 = *((unsigned int *) param0 + 0x8);
                              break label$62;
                            break label$63;
                            };
                            *((unsigned int *) 0x10048c) = local4 = (param0 = ((local1 + 0xf) & -0x8) - 0x8);
                            *((unsigned int *) 0x100484) = param0 = ((local9 = (local3 - 0x28) + (local1 - param0)) + 0x8);
                            *((unsigned int *) local4 + 0x4) = (param0 | 0x1);
                            *((unsigned int *) (local1 + local9) + 0x4) = 0x28;
                            *((unsigned int *) 0x100498) = 0x200000;
                            *((unsigned int *) local4 = ((unsigned) param0 < (local2 + 0x10)) ? local2 : param0 = (((local7 - 0x20) & -0x8) - 0x8) + 0x4) = 0x1b;
                            local10 = *((unsigned long *) 0x100360);
                            *((unsigned long *) (local4 + 0x10)) = *((unsigned long *) 0x100368);
                            *((unsigned long *) local4 + 0x8) = local10;
                            *((unsigned int *) 0x10036c) = local6;
                            *((unsigned int *) 0x100364) = local3;
                            *((unsigned int *) 0x100360) = local1;
                            *((unsigned int *) 0x100368) = (local4 + 0x8);
                            param0 = (local4 + 0x1c);
                            while (1) {
                              *((unsigned int *) param0) = 0x7;
                              if (((unsigned) param0 = (param0 + 0x4) < local7)) break label$65;
                            break ;
                            };
                            if ((local2 == local4)) break label$45;
                            *((unsigned int *) local4 + 0x4) = (*((unsigned int *) local4 + 0x4) & -0x2);
                            *((unsigned int *) local2 + 0x4) = (param0 = (local4 - local2) | 0x1);
                            *((unsigned int *) local4) = param0;
                            if (((unsigned) param0 >= 0x100)) {
                              {
                                $func8(local2, param0);
                                break label$45;
                              };
                            };
                            local1 = ((param0 & -0x8) + 0x100370);
                            param0 = label$67: {
                              if (((local4 = *((unsigned int *) 0x100478) & param0 = (0x1 << (param0 >>> 0x3))) == 0x0)) {
                                {
                                  *((unsigned int *) 0x100478) = (param0 | local4);
                                  break(local1) label$67;
                                };
                              };
                              *((unsigned int *) local1 + 0x8);
                            };
                            *((unsigned int *) local1 + 0x8) = local2;
                            *((unsigned int *) param0 + 0xc) = local2;
                            *((unsigned int *) local2 + 0xc) = local1;
                            *((unsigned int *) local2 + 0x8) = param0;
                            break label$45;
                          };
                          *((unsigned int *) param0) = local1;
                          *((unsigned int *) param0 + 0x4) = (*((unsigned int *) param0 + 0x4) + local3);
                          *((unsigned int *) local2 = (((local1 + 0xf) & -0x8) - 0x8) + 0x4) = (local5 | 0x3);
                          local5 = (local3 = (((local4 + 0xf) & -0x8) - 0x8) - param0 = (local2 + local5));
                          if ((local3 == *((unsigned int *) 0x10048c))) break label$48;
                          if ((local3 == *((unsigned int *) 0x100488))) break label$47;
                          if (((local1 = *((unsigned int *) local3 + 0x4) & 0x3) == 0x1)) {
                            {
                              $func6(local3, local1 = (local1 & -0x8));
                              local5 = (local1 + local5);
                              local1 = *((unsigned int *) local3 = (local1 + local3) + 0x4);
                            };
                          };
                          *((unsigned int *) local3 + 0x4) = (local1 & -0x2);
                          *((unsigned int *) param0 + 0x4) = (local5 | 0x1);
                          *((unsigned int *) (param0 + local5)) = local5;
                          if (((unsigned) local5 >= 0x100)) {
                            {
                              $func8(param0, local5);
                              break label$46;
                            };
                          };
                          local1 = ((local5 & -0x8) + 0x100370);
                          local4 = label$71: {
                            if (((local4 = *((unsigned int *) 0x100478) & local3 = (0x1 << (local5 >>> 0x3))) == 0x0)) {
                              {
                                *((unsigned int *) 0x100478) = (local3 | local4);
                                break(local1) label$71;
                              };
                            };
                            *((unsigned int *) local1 + 0x8);
                          };
                          *((unsigned int *) local1 + 0x8) = param0;
                          *((unsigned int *) local4 + 0xc) = param0;
                          *((unsigned int *) param0 + 0xc) = local1;
                          *((unsigned int *) param0 + 0x8) = local4;
                          break label$46;
                        };
                      };
                      *((unsigned int *) 0x100484) = local1 = (param0 - local5);
                      *((unsigned int *) 0x10048c) = local2 = (param0 = *((unsigned int *) 0x10048c) + local5);
                      *((unsigned int *) local2 + 0x4) = (local1 | 0x1);
                      *((unsigned int *) param0 + 0x4) = (local5 | 0x3);
                      local3 = (param0 + 0x8);
                      break label$1;
                    };
                  };
                  param0 = *((unsigned int *) 0x100488);
                  label$73: {
                    if (((unsigned) local2 = (local1 - local5) <= 0xf)) {
                      {
                        *((unsigned int *) 0x100488) = 0x0;
                        *((unsigned int *) 0x100480) = 0x0;
                        *((unsigned int *) param0 + 0x4) = (local1 | 0x3);
                        *((unsigned int *) local1 = (param0 + local1) + 0x4) = (*((unsigned int *) local1 + 0x4) | 0x1);
                        break label$73;
                      };
                    };
                    *((unsigned int *) 0x100480) = local2;
                    *((unsigned int *) 0x100488) = local4 = (param0 + local5);
                    *((unsigned int *) local4 + 0x4) = (local2 | 0x1);
                    *((unsigned int *) (param0 + local1)) = local2;
                    *((unsigned int *) param0 + 0x4) = (local5 | 0x3);
                  };
                  local3 = (param0 + 0x8);
                  break label$1;
                };
                *((unsigned int *) param0 + 0x4) = (local3 + local7);
                *((unsigned int *) 0x10048c) = local2 = (local1 = ((param0 = *((unsigned int *) 0x10048c) + 0xf) & -0x8) - 0x8);
                *((unsigned int *) 0x100484) = local1 = ((local4 = (*((unsigned int *) 0x100484) + local3) + (param0 - local1)) + 0x8);
                *((unsigned int *) local2 + 0x4) = (local1 | 0x1);
                *((unsigned int *) (param0 + local4) + 0x4) = 0x28;
                *((unsigned int *) 0x100498) = 0x200000;
                break label$45;
              };
              *((unsigned int *) 0x10048c) = param0;
              *((unsigned int *) 0x100484) = local1 = (*((unsigned int *) 0x100484) + local5);
              *((unsigned int *) param0 + 0x4) = (local1 | 0x1);
              break label$46;
            };
            *((unsigned int *) 0x100488) = param0;
            *((unsigned int *) 0x100480) = local1 = (*((unsigned int *) 0x100480) + local5);
            *((unsigned int *) param0 + 0x4) = (local1 | 0x1);
            *((unsigned int *) (param0 + local1)) = local1;
          };
          local3 = (local2 + 0x8);
          break label$1;
        };
        local3 = 0x0;
        if (((unsigned) param0 = *((unsigned int *) 0x100484) <= local5)) break label$1;
        *((unsigned int *) 0x100484) = local1 = (param0 - local5);
        *((unsigned int *) 0x10048c) = local2 = (param0 = *((unsigned int *) 0x10048c) + local5);
        *((unsigned int *) local2 + 0x4) = (local1 | 0x1);
        *((unsigned int *) param0 + 0x4) = (local5 | 0x3);
        local3 = (param0 + 0x8);
        break label$1;
      };
      *((unsigned int *) param0 + 0x18) = local7;
      if (local1 = *((unsigned int *) local2 + 0x10)) {
        {
          *((unsigned int *) param0 + 0x10) = local1;
          *((unsigned int *) local1 + 0x18) = param0;
        };
      };
      if ((local1 = *((unsigned int *) (local2 + 0x14)) == 0x0)) break label$2;
      *((unsigned int *) (param0 + 0x14)) = local1;
      *((unsigned int *) local1 + 0x18) = param0;
    };
    label$76: {
      if (((unsigned) local3 >= 0x10)) {
        {
          *((unsigned int *) local2 + 0x4) = (local5 | 0x3);
          *((unsigned int *) param0 = (local2 + local5) + 0x4) = (local3 | 0x1);
          *((unsigned int *) (param0 + local3)) = local3;
          if (((unsigned) local3 >= 0x100)) {
            {
              $func8(param0, local3);
              break label$76;
            };
          };
          local1 = ((local3 & -0x8) + 0x100370);
          local4 = label$79: {
            if (((local4 = *((unsigned int *) 0x100478) & local3 = (0x1 << (local3 >>> 0x3))) == 0x0)) {
              {
                *((unsigned int *) 0x100478) = (local3 | local4);
                break(local1) label$79;
              };
            };
            *((unsigned int *) local1 + 0x8);
          };
          *((unsigned int *) local1 + 0x8) = param0;
          *((unsigned int *) local4 + 0xc) = param0;
          *((unsigned int *) param0 + 0xc) = local1;
          *((unsigned int *) param0 + 0x8) = local4;
          break label$76;
        };
      };
      *((unsigned int *) local2 + 0x4) = (param0 = (local3 + local5) | 0x3);
      *((unsigned int *) param0 = (param0 + local2) + 0x4) = (*((unsigned int *) param0 + 0x4) | 0x1);
    };
    local3 = (local2 + 0x8);
  };
  global0 = (local8 + 0x10);
  return local3;
}

// O[1] Decompilation of $func1, known as $func1
export "check"; // $func1 is exported to "check"
int $func1(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;
  // local index=7
  int local7;
  // local index=8
  int local8;
  // local index=9
  int local9;
  // local index=10
  int local10;
  // local index=11
  int local11;
  // local index=12
  int local12;
  // local index=13
  int local13;

  global0 = local3 = (global0 - 0x50);
  *((unsigned long *) local3 + 0x3c) = 5486031072848061934;
  *((unsigned long *) local3 + 0x34) = 340528315340175203;
  *((unsigned long *) local3 + 0x2c) = 5509388002251769388;
  *((unsigned long *) local3 + 0x24) = 5567854816287694086;
  *((unsigned long *) local3 + 0x1c) = 7292522372460443097;
  *((unsigned long *) local3 + 0x14) = 4334395362698426110;
  *((unsigned long *) local3 + 0xc) = -3427922058694346327;
  *((unsigned int *) local3 + 0x4c) = 0x0;
  *((unsigned long *) local3 + 0x44) = 17179869184;
  if (param1) {
    label$2: {
      local9 = 0x4;
      local8 = param1;
      param1 = param0;
      while (1) {
        local5 = (local10 = ((unsigned) local8 >= 0x4) ? 0x4 : local8 & 0x3);
        local7 = 0x0;
        local11 = 0x0;
        local2 = param1;
        if (((unsigned) (local10 - 0x1) >= 0x3)) {
          {
            local12 = (local10 & 0x4);
            local2 = 0x18;
            while (1) {
              local7 = ((*((unsigned char *) (local6 = (param1 + local11) + 0x3)) << local2) | (((local7 | *((unsigned char *) local6)) | (*((unsigned char *) (local6 + 0x1)) << (local2 - 0x10))) | (*((unsigned char *) (local6 + 0x2)) << (local2 - 0x8))));
              local2 = (local2 + 0x20);
              if ((local12 != local11 = (local11 + 0x4))) break label$5;
            break ;
            };
            local2 = (param1 + local11);
          };
        };
        if (local5) {
          {
            local6 = (local11 << 0x3);
            while (1) {
              local7 = ((*((unsigned char *) local2) << local6) | local7);
              local6 = (local6 + 0x8);
              local2 = (local2 + 0x1);
              if (local5 = (local5 - 0x1)) break label$7;
            break ;
            };
          };
        };
        local8 = (local8 - local10);
        param1 = (param1 + local10);
        if ((*((unsigned int *) local3 + 0x44) == local4)) {
          {
            $func10((local3 + 0x44), local4);
            local4 = *((unsigned int *) local3 + 0x4c);
            local9 = *((unsigned int *) local3 + 0x48);
          };
        };
        *((unsigned int *) (local9 + (local4 << 0x2))) = local7;
        *((unsigned int *) local3 + 0x4c) = local4 = (local4 + 0x1);
        if (local8) break label$3;
      break ;
      };
      local12 = *((unsigned int *) local3 + 0x44);
      label$9: {
        if (((local4 & 0x1) == 0x0)) {
          {
            local9 = *((unsigned int *) local3 + 0x48);
            break label$9;
          };
        };
        if ((local4 == local12)) {
          {
            $func10((local3 + 0x44), local4);
            local12 = *((unsigned int *) local3 + 0x44);
            local4 = *((unsigned int *) local3 + 0x4c);
          };
        };
        *((unsigned int *) (local9 = *((unsigned int *) local3 + 0x48) + (local4 << 0x2))) = 0x0;
        local4 = (local4 + 0x1);
      };
      local8 = 0x0;
      label$12: {
        label$13: {
          if ((local4 == 0x0)) break label$13;
          param1 = local4;
          local5 = local9;
          while (1) {
            if ((local2 = ((unsigned) param1 >= 0x2) ? 0x2 : param1 == 0x1)) break label$12;
            param1 = (param1 - local2);
            local5 = {
              local13 = (local5 + (local2 << 0x2));
              local2 = *((unsigned int *) local5 + 0x4);
              local7 = *((unsigned int *) local5);
              local6 = -0x61c88647;
              local11 = 0x20;
              while (1) {
                local2 = (((((local7 = (((local2 + local6) ^ (((local2 >>> 0x5) - 0x6fceac95) ^ ((local2 << 0x4) + 0x54684935))) + local7) << 0x4) + 0x6579666f) ^ (local6 + local7)) ^ ((local7 >>> 0x5) + 0x72544541)) + local2);
                local6 = (local6 - 0x61c88647);
                if (local11 = (local11 - 0x1)) break label$15;
              break ;
              };
              *((unsigned int *) local5 + 0x4) = local2;
              *((unsigned int *) local5) = local7;
              local13;
            };
            if (param1) break label$14;
          break ;
          };
          if ((local4 != 0xe)) break label$13;
          param1 = local9;
          local5 = (local3 + 0xc);
          local2 = 0x0;
          local4 = 0x38;
          label$16: {
            while (1) if ((local8 = *((unsigned char *) param1) == local10 = *((unsigned char *) local5))) {
              {
                param1 = (param1 + 0x1);
                local5 = (local5 + 0x1);
                if (local4 = (local4 - 0x1)) break label$17;
                break label$16;
              };
            };
            local2 = (local8 - local10);
          };
          local8 = (local2 == 0x0);
        };
        if (local12) {
          $func2(local9);
        };
        $func2(param0);
        break label$2;
      };
      global0 = param0 = (global0 - 0x30);
      *((unsigned int *) param0 + 0x4) = 0x1;
      *((unsigned int *) param0) = 0x1;
      *((unsigned long *) (param0 + 0x14)) = 0x2;
      *((unsigned int *) (param0 + 0x2c)) = 0x1;
      *((unsigned int *) param0 + 0xc) = 0x2;
      *((unsigned int *) param0 + 0x8) = 0x1001cc;
      *((unsigned int *) param0 + 0x24) = 0x1;
      *((unsigned int *) param0 + 0x10) = (param0 + 0x20);
      *((unsigned int *) param0 + 0x28) = param0;
      *((unsigned int *) param0 + 0x20) = (param0 + 0x4);
      $func21((param0 + 0x8), 0x10000c);
      abort("unreachable");
    };
  };
  global0 = (local3 + 0x50);
  return local8;
}

// O[2] Disassembly of $func2, known as $func2
void $func2(int param0) {
  // local index=1
  int local1;
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;

  local2 = (local1 = (param0 - 0x8) + param0 = (local3 = *((unsigned int *) (param0 - 0x4)) & -0x8));
  label$1: {
    label$2: {
      label$3: {
        label$4: {
          if ((local3 & 0x1)) break label$4;
          if (((local3 & 0x3) == 0x0)) break label$3;
          param0 = (local3 = *((unsigned int *) local1) + param0);
          if ((local1 = (local1 - local3) == *((unsigned int *) 0x100488))) {
            {
              if (((*((unsigned int *) local2 + 0x4) & 0x3) != 0x3)) break label$4;
              *((unsigned int *) 0x100480) = param0;
              *((unsigned int *) local2 + 0x4) = (*((unsigned int *) local2 + 0x4) & -0x2);
              *((unsigned int *) local1 + 0x4) = (param0 | 0x1);
              *((unsigned int *) local2) = param0;
              return;
            };
          };
          $func6(local1, local3);
        };
        label$6: {
          label$7: {
            if (((local3 = *((unsigned int *) local2 + 0x4) & 0x2) == 0x0)) {
              {
                if ((local2 == *((unsigned int *) 0x10048c))) break label$6;
                if ((local2 == *((unsigned int *) 0x100488))) break label$1;
                $func6(local2, local2 = (local3 & -0x8));
                *((unsigned int *) local1 + 0x4) = (param0 = (param0 + local2) | 0x1);
                *((unsigned int *) (param0 + local1)) = param0;
                if ((local1 != *((unsigned int *) 0x100488))) break label$7;
                *((unsigned int *) 0x100480) = param0;
                return;
              };
            };
            *((unsigned int *) local2 + 0x4) = (local3 & -0x2);
            *((unsigned int *) local1 + 0x4) = (param0 | 0x1);
            *((unsigned int *) (param0 + local1)) = param0;
          };
          if (((unsigned) param0 < 0x100)) break label$2;
          $func8(local1, param0);
          local1 = 0x0;
          *((unsigned int *) 0x1004a0) = param0 = (*((unsigned int *) 0x1004a0) - 0x1);
          if (param0) break label$3;
          if (param0 = *((unsigned int *) 0x100368)) {
            while (1) {
              local1 = (local1 + 0x1);
              if (param0 = *((unsigned int *) param0 + 0x8)) break label$10;
            break ;
            };
          };
          *((unsigned int *) 0x1004a0) = ((unsigned) local1 <= 0xfff) ? 0xfff : local1;
          return;
        };
        *((unsigned int *) 0x10048c) = local1;
        *((unsigned int *) 0x100484) = param0 = (*((unsigned int *) 0x100484) + param0);
        *((unsigned int *) local1 + 0x4) = (param0 | 0x1);
        if ((*((unsigned int *) 0x100488) == local1)) {
          {
            *((unsigned int *) 0x100480) = 0x0;
            *((unsigned int *) 0x100488) = 0x0;
          };
        };
        if (((unsigned) param0 <= local3 = *((unsigned int *) 0x100498))) break label$3;
        if ((local2 = *((unsigned int *) 0x10048c) == 0x0)) break label$3;
        local1 = 0x0;
        label$12: {
          if (((unsigned) local4 = *((unsigned int *) 0x100484) < 0x29)) break label$12;
          param0 = 0x100360;
          while (1) {
            if (((unsigned) local2 >= local5 = *((unsigned int *) param0))) {
              if (((unsigned) (local5 + *((unsigned int *) param0 + 0x4)) > local2)) break label$12;
            };
            if (param0 = *((unsigned int *) param0 + 0x8)) break label$13;
          break ;
          };
        };
        if (param0 = *((unsigned int *) 0x100368)) {
          while (1) {
            local1 = (local1 + 0x1);
            if (param0 = *((unsigned int *) param0 + 0x8)) break label$16;
          break ;
          };
        };
        *((unsigned int *) 0x1004a0) = ((unsigned) local1 <= 0xfff) ? 0xfff : local1;
        if (((unsigned) local3 >= local4)) break label$3;
        *((unsigned int *) 0x100498) = -0x1;
      };
      return;
    };
    local2 = ((param0 & -0x8) + 0x100370);
    param0 = label$17: {
      if (((local3 = *((unsigned int *) 0x100478) & param0 = (0x1 << (param0 >>> 0x3))) == 0x0)) {
        {
          *((unsigned int *) 0x100478) = (param0 | local3);
          break(local2) label$17;
        };
      };
      *((unsigned int *) local2 + 0x8);
    };
    *((unsigned int *) local2 + 0x8) = local1;
    *((unsigned int *) param0 + 0xc) = local1;
    *((unsigned int *) local1 + 0xc) = local2;
    *((unsigned int *) local1 + 0x8) = param0;
    return;
  };
  *((unsigned int *) 0x100488) = local1;
  *((unsigned int *) 0x100480) = param0 = (*((unsigned int *) 0x100480) + param0);
  *((unsigned int *) local1 + 0x4) = (param0 | 0x1);
  *((unsigned int *) (param0 + local1)) = param0;
}

// O[1] Decompilation of $func3, known as $func3
int $func3(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;
  // local index=7
  int local7;
  // local index=8
  int local8;
  // local index=9
  int local9;
  // local index=10
  int local10;
  // local index=11
  int local11;
  // local index=12
  int local12;
  // local index=13
  int local13;
  // local index=14
  int local14;

  global0 = local2 = (global0 - 0x30);
  *((unsigned int *) (local2 + 0x24)) = 0x10001c;
  *((unsigned char *) local2 + 0x2c) = 0x3;
  *((unsigned int *) local2 + 0x1c) = 0x20;
  *((unsigned int *) local2 + 0x28) = 0x0;
  *((unsigned int *) local2 + 0x20) = param0;
  *((unsigned int *) local2 + 0x14) = 0x0;
  *((unsigned int *) local2 + 0xc) = 0x0;
  return {
    local14 = label$1: {
      label$2: {
        label$3: {
          label$4: {
            if ((local10 = *((unsigned int *) param1 + 0x10) == 0x0)) {
              {
                if ((param0 = *((unsigned int *) (param1 + 0xc)) == 0x0)) break label$4;
                local4 = (local3 = *((unsigned int *) param1 + 0x8) + (param0 << 0x3));
                local8 = (((param0 - 0x1) & 0x1fffffff) + 0x1);
                param0 = *((unsigned int *) param1);
                while (1) {
                  if (local5 = *((unsigned int *) (param0 + 0x4))) {
                    if (__function_table[*((unsigned int *) *((unsigned int *) local2 + 0x24) + 0xc)](*((unsigned int *) local2 + 0x20), *((unsigned int *) param0), local5)) break label$3;
                  };
                  if (__function_table[*((unsigned int *) (local3 + 0x4))](*((unsigned int *) local3), (local2 + 0xc))) break label$3;
                  local7 = (local7 + 0x1);
                  param0 = (param0 + 0x8);
                  if ((local3 = (local3 + 0x8) != local4)) break label$6;
                break ;
                };
                break label$4;
              };
            };
            if ((param0 = *((unsigned int *) (param1 + 0x14)) == 0x0)) break label$4;
            local11 = (param0 << 0x5);
            local8 = (((param0 - 0x1) & 0x7ffffff) + 0x1);
            local5 = *((unsigned int *) param1 + 0x8);
            param0 = *((unsigned int *) param1);
            while (1) {
              if (local3 = *((unsigned int *) (param0 + 0x4))) {
                if (__function_table[*((unsigned int *) *((unsigned int *) local2 + 0x24) + 0xc)](*((unsigned int *) local2 + 0x20), *((unsigned int *) param0), local3)) break label$3;
              };
              *((unsigned int *) local2 + 0x1c) = *((unsigned int *) (local3 = (local7 + local10) + 0x10));
              *((unsigned char *) local2 + 0x2c) = *((unsigned char *) (local3 + 0x1c));
              *((unsigned int *) local2 + 0x28) = *((unsigned int *) (local3 + 0x18));
              local6 = *((unsigned int *) (local3 + 0xc));
              local9 = 0x0;
              local4 = 0x0;
              label$10: {
                label$11: {
                  label$12: {
                    switch ((*((unsigned int *) (local3 + 0x8)) - 0x1)) {
                      case 0: break label$12;
                      case 1: break label$10;
                      default: break label$11;
                    };
                  };
                  if ((*((unsigned int *) local12 = ((local6 << 0x3) + local5) + 0x4) != 0x11)) break label$10;
                  local6 = *((unsigned int *) *((unsigned int *) local12));
                };
                local4 = 0x1;
              };
              *((unsigned int *) local2 + 0x10) = local6;
              *((unsigned int *) local2 + 0xc) = local4;
              local4 = *((unsigned int *) (local3 + 0x4));
              label$13: {
                label$14: {
                  label$15: {
                    switch ((*((unsigned int *) local3) - 0x1)) {
                      case 0: break label$15;
                      case 1: break label$13;
                      default: break label$14;
                    };
                  };
                  if ((*((unsigned int *) local6 = ((local4 << 0x3) + local5) + 0x4) != 0x11)) break label$13;
                  local4 = *((unsigned int *) *((unsigned int *) local6));
                };
                local9 = 0x1;
              };
              *((unsigned int *) local2 + 0x18) = local4;
              *((unsigned int *) local2 + 0x14) = local9;
              if (__function_table[*((unsigned int *) (local3 + 0x4))](*((unsigned int *) local3 = (local5 + (*((unsigned int *) (local3 + 0x14)) << 0x3))), (local2 + 0xc))) break label$3;
              local13 = (local13 + 0x1);
              param0 = (param0 + 0x8);
              if ((local11 != local7 = (local7 + 0x20))) break label$8;
            break ;
            };
          };
          if (((unsigned) local8 >= *((unsigned int *) param1 + 0x4))) break label$2;
          if ((__function_table[*((unsigned int *) *((unsigned int *) local2 + 0x24) + 0xc)](*((unsigned int *) local2 + 0x20), *((unsigned int *) param0 = (*((unsigned int *) param1) + (local8 << 0x3))), *((unsigned int *) param0 + 0x4)) == 0x0)) break label$2;
        };
        break(0x1) label$1;
      };
      0x0;
    };
    global0 = (local2 + 0x30);
    local14;
  };
}

// O[2] Disassembly of $func4, known as $func4
void $func4(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;

  local2 = (param0 + param1);
  label$1: {
    label$2: {
      if ((local3 = *((unsigned int *) param0 + 0x4) & 0x1)) break label$2;
      if (((local3 & 0x3) == 0x0)) break label$1;
      param1 = (local3 = *((unsigned int *) param0) + param1);
      if ((param0 = (param0 - local3) == *((unsigned int *) 0x100488))) {
        {
          if (((*((unsigned int *) local2 + 0x4) & 0x3) != 0x3)) break label$2;
          *((unsigned int *) 0x100480) = param1;
          *((unsigned int *) local2 + 0x4) = (*((unsigned int *) local2 + 0x4) & -0x2);
          *((unsigned int *) param0 + 0x4) = (param1 | 0x1);
          *((unsigned int *) local2) = param1;
          break label$1;
        };
      };
      $func6(param0, local3);
    };
    label$4: {
      label$5: {
        label$6: {
          if (((local3 = *((unsigned int *) local2 + 0x4) & 0x2) == 0x0)) {
            {
              if ((local2 == *((unsigned int *) 0x10048c))) break label$5;
              if ((local2 == *((unsigned int *) 0x100488))) break label$4;
              $func6(local2, local2 = (local3 & -0x8));
              *((unsigned int *) param0 + 0x4) = (param1 = (param1 + local2) | 0x1);
              *((unsigned int *) (param0 + param1)) = param1;
              if ((param0 != *((unsigned int *) 0x100488))) break label$6;
              *((unsigned int *) 0x100480) = param1;
              return;
            };
          };
          *((unsigned int *) local2 + 0x4) = (local3 & -0x2);
          *((unsigned int *) param0 + 0x4) = (param1 | 0x1);
          *((unsigned int *) (param0 + param1)) = param1;
        };
        if (((unsigned) param1 >= 0x100)) {
          {
            $func8(param0, param1);
            return;
          };
        };
        local2 = ((param1 & -0x8) + 0x100370);
        param1 = label$9: {
          if (((local3 = *((unsigned int *) 0x100478) & param1 = (0x1 << (param1 >>> 0x3))) == 0x0)) {
            {
              *((unsigned int *) 0x100478) = (param1 | local3);
              break(local2) label$9;
            };
          };
          *((unsigned int *) local2 + 0x8);
        };
        *((unsigned int *) local2 + 0x8) = param0;
        *((unsigned int *) param1 + 0xc) = param0;
        *((unsigned int *) param0 + 0xc) = local2;
        *((unsigned int *) param0 + 0x8) = param1;
        return;
      };
      *((unsigned int *) 0x10048c) = param0;
      *((unsigned int *) 0x100484) = param1 = (*((unsigned int *) 0x100484) + param1);
      *((unsigned int *) param0 + 0x4) = (param1 | 0x1);
      if ((param0 != *((unsigned int *) 0x100488))) break label$1;
      *((unsigned int *) 0x100480) = 0x0;
      *((unsigned int *) 0x100488) = 0x0;
      return;
    };
    *((unsigned int *) 0x100488) = param0;
    *((unsigned int *) 0x100480) = param1 = (*((unsigned int *) 0x100480) + param1);
    *((unsigned int *) param0 + 0x4) = (param1 | 0x1);
    *((unsigned int *) (param0 + param1)) = param1;
  };
}

// O[2] Disassembly of $func5, known as $func5
int $func5(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;

  label$1: {
    if (((unsigned) (-0x10033 - param0 = ((unsigned) param0 <= 0x10) ? 0x10 : param0) <= param1)) break label$1;
    if ((local2 = $func0(((param0 + local4 = ((unsigned) param1 < 0xb) ? 0x10 : ((param1 + 0xb) & -0x8)) + 0xc)) == 0x0)) break label$1;
    param1 = (local2 - 0x8);
    label$2: {
      if (((local3 = (param0 - 0x1) & local2) == 0x0)) {
        {
          param0 = param1;
          break label$2;
        };
      };
      local3 = ((local6 = *((unsigned int *) local5 = (local2 - 0x4)) & -0x8) - local2 = (param0 = (local2 = (((local2 + local3) & (0x0 - param0)) - 0x8) + ((unsigned) (local2 - param1) <= 0x10) ? param0 : 0x0) - param1));
      if ((local6 & 0x3)) {
        {
          *((unsigned int *) param0 + 0x4) = ((local3 | (*((unsigned int *) param0 + 0x4) & 0x1)) | 0x2);
          *((unsigned int *) local3 = (param0 + local3) + 0x4) = (*((unsigned int *) local3 + 0x4) | 0x1);
          *((unsigned int *) local5) = ((local2 | (*((unsigned int *) local5) & 0x1)) | 0x2);
          *((unsigned int *) local3 = (param1 + local2) + 0x4) = (*((unsigned int *) local3 + 0x4) | 0x1);
          $func4(param1, local2);
          break label$2;
        };
      };
      param1 = *((unsigned int *) param1);
      *((unsigned int *) param0 + 0x4) = local3;
      *((unsigned int *) param0) = (param1 + local2);
    };
    label$5: {
      if (((param1 = *((unsigned int *) param0 + 0x4) & 0x3) == 0x0)) break label$5;
      if (((unsigned) local2 = (param1 & -0x8) <= (local4 + 0x10))) break label$5;
      *((unsigned int *) param0 + 0x4) = ((local4 | (param1 & 0x1)) | 0x2);
      *((unsigned int *) param1 = (param0 + local4) + 0x4) = (local4 = (local2 - local4) | 0x3);
      *((unsigned int *) local2 = (param0 + local2) + 0x4) = (*((unsigned int *) local2 + 0x4) | 0x1);
      $func4(param1, local4);
    };
    local3 = (param0 + 0x8);
  };
  return local3;
}

// O[2] Disassembly of $func6, known as $func6
void $func6(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;

  local2 = *((unsigned int *) param0 + 0xc);
  label$1: {
    label$2: {
      if (((unsigned) param1 >= 0x100)) {
        {
          local3 = *((unsigned int *) param0 + 0x18);
          label$4: {
            label$5: {
              if ((param0 == local2)) {
                {
                  if (param1 = *((unsigned int *) (param0 + local4 = *((unsigned int *) local2 = (param0 + 0x14)) ? 0x14 : 0x10))) break label$5;
                  local2 = 0x0;
                  break label$4;
                };
              };
              *((unsigned int *) param1 = *((unsigned int *) param0 + 0x8) + 0xc) = local2;
              *((unsigned int *) local2 + 0x8) = param1;
              break label$4;
            };
            local4 = local4 ? local2 : (param0 + 0x10);
            while (1) {
              local5 = local4;
              local4 = param1 = *((unsigned int *) param1) ? param1 = (local2 = param1 + 0x14) : (local2 + 0x10);
              if (param1 = *((unsigned int *) (local2 + param1 ? 0x14 : 0x10))) break label$7;
            break ;
            };
            *((unsigned int *) local5) = 0x0;
          };
          if ((local3 == 0x0)) break label$1;
          if ((param0 != *((unsigned int *) param1 = ((*((unsigned int *) param0 + 0x1c) << 0x2) + 0x1002e0)))) {
            {
              *((unsigned int *) (local3 + (*((unsigned int *) local3 + 0x10) == param0) ? 0x10 : 0x14)) = local2;
              if ((local2 == 0x0)) break label$1;
              break label$2;
            };
          };
          *((unsigned int *) param1) = local2;
          if (local2) break label$2;
          *((unsigned int *) 0x10047c) = (*((unsigned int *) 0x10047c) & __rotl_i32(-0x2, *((unsigned int *) param0 + 0x1c)));
          break label$1;
        };
      };
      if ((param0 = *((unsigned int *) param0 + 0x8) != local2)) {
        {
          *((unsigned int *) param0 + 0xc) = local2;
          *((unsigned int *) local2 + 0x8) = param0;
          return;
        };
      };
      *((unsigned int *) 0x100478) = (*((unsigned int *) 0x100478) & __rotl_i32(-0x2, (param1 >>> 0x3)));
      return;
    };
    *((unsigned int *) local2 + 0x18) = local3;
    if (param1 = *((unsigned int *) param0 + 0x10)) {
      {
        *((unsigned int *) local2 + 0x10) = param1;
        *((unsigned int *) param1 + 0x18) = local2;
      };
    };
    if ((param0 = *((unsigned int *) (param0 + 0x14)) == 0x0)) break label$1;
    *((unsigned int *) (local2 + 0x14)) = param0;
    *((unsigned int *) param0 + 0x18) = local2;
  };
}

// O[1] Decompilation of $func7, known as $func7
int $func7(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;

  global0 = local3 = (global0 - 0x10);
  label$1: {
    param1 = label$2: {
      label$3: {
        if (((unsigned) param1 >= 0x80)) {
          {
            *((unsigned int *) local3 + 0xc) = 0x0;
            if (((unsigned) param1 < 0x800)) break label$3;
            if (((unsigned) param1 < 0x10000)) {
              {
                *((unsigned char *) local3 + 0xe) = ((param1 & 0x3f) | 0x80);
                *((unsigned char *) local3 + 0xc) = ((param1 >>> 0xc) | 0xe0);
                *((unsigned char *) local3 + 0xd) = (((param1 >>> 0x6) & 0x3f) | 0x80);
                break(0x3) label$2;
              };
            };
            *((unsigned char *) local3 + 0xf) = ((param1 & 0x3f) | 0x80);
            *((unsigned char *) local3 + 0xe) = (((param1 >>> 0x6) & 0x3f) | 0x80);
            *((unsigned char *) local3 + 0xd) = (((param1 >>> 0xc) & 0x3f) | 0x80);
            *((unsigned char *) local3 + 0xc) = (((param1 >>> 0x12) & 0x7) | 0xf0);
            break(0x4) label$2;
          };
        };
        if ((local2 = *((unsigned int *) param0 + 0x8) == *((unsigned int *) param0))) {
          {
            global0 = local4 = (global0 - 0x20);
            label$7: {
              label$8: {
                if ((local2 = (local2 + 0x1) == 0x0)) break label$8;
                local2 = ((local5 = ((unsigned) local2 <= 0x8) ? 0x8 : local2 = ((unsigned) local2 < local5) ? local5 = (local6 = *((unsigned int *) param0) << 0x1) : local2 ^ -0x1) >>> 0x1f);
                label$9: {
                  if ((local6 == 0x0)) {
                    {
                      *((unsigned int *) local4 + 0x18) = 0x0;
                      break label$9;
                    };
                  };
                  *((unsigned int *) local4 + 0x1c) = local6;
                  *((unsigned int *) local4 + 0x18) = 0x1;
                  *((unsigned int *) local4 + 0x14) = *((unsigned int *) param0 + 0x4);
                };
                $func13((local4 + 0x8), local2, local5, (local4 + 0x14));
                local2 = *((unsigned int *) local4 + 0xc);
                if ((*((unsigned int *) local4 + 0x8) == 0x0)) {
                  {
                    *((unsigned int *) param0) = local5;
                    *((unsigned int *) param0 + 0x4) = local2;
                    break label$7;
                  };
                };
                if ((local2 == -0x7fffffff)) break label$7;
                if ((local2 == 0x0)) break label$8;
                $func34(local2, *((unsigned int *) (local4 + 0x10)));
                abort("unreachable");
              };
              $func20();
              abort("unreachable");
            };
            global0 = (local4 + 0x20);
            local2 = *((unsigned int *) param0 + 0x8);
          };
        };
        *((unsigned int *) param0 + 0x8) = (local2 + 0x1);
        *((unsigned char *) (*((unsigned int *) param0 + 0x4) + local2)) = param1;
        break label$1;
      };
      *((unsigned char *) local3 + 0xd) = ((param1 & 0x3f) | 0x80);
      *((unsigned char *) local3 + 0xc) = ((param1 >>> 0x6) | 0xc0);
      0x2;
    };
    if (((unsigned) param1 > (*((unsigned int *) param0) - local2 = *((unsigned int *) param0 + 0x8)))) {
      {
        $func12(param0, local2, param1);
        local2 = *((unsigned int *) param0 + 0x8);
      };
    };
    $func35((*((unsigned int *) param0 + 0x4) + local2), (local3 + 0xc), param1);
    *((unsigned int *) param0 + 0x8) = (param1 + local2);
  };
  global0 = (local3 + 0x10);
  return 0x0;
}

// O[2] Disassembly of $func8, known as $func8
void $func8(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;

  *((unsigned long *) param0 + 0x10) = 0x0;
  *((unsigned int *) param0 + 0x1c) = local2 = label$1: {
    if (((unsigned) param1 < 0x100)) break(0x0) label$1;
    if (((unsigned) param1 > 0xffffff)) break(0x1f) label$1;
    ((((param1 >>> (0x6 - local3 = __clz_i32((param1 >>> 0x8)))) & 0x1) - (local3 << 0x1)) + 0x3e);
  };
  local4 = ((local2 << 0x2) + 0x1002e0);
  label$2: {
    if (((local5 = *((unsigned int *) 0x10047c) & local3 = (0x1 << local2)) == 0x0)) {
      {
        *((unsigned int *) 0x10047c) = (local3 | local5);
        *((unsigned int *) local4) = param0;
        *((unsigned int *) param0 + 0x18) = local4;
        break label$2;
      };
    };
    label$4: {
      label$5: {
        if ((param1 == (*((unsigned int *) local3 = *((unsigned int *) local4) + 0x4) & -0x8))) {
          {
            local2 = local3;
            break label$5;
          };
        };
        local4 = (param1 << (local2 != 0x1f) ? (0x19 - (local2 >>> 0x1)) : 0x0);
        while (1) {
          if ((local2 = *((unsigned int *) local5 = ((local3 + ((local4 >>> 0x1d) & 0x4)) + 0x10)) == 0x0)) break label$4;
          local4 = (local4 << 0x1);
          local3 = local2;
          if (((*((unsigned int *) local2 + 0x4) & -0x8) != param1)) break label$7;
        break ;
        };
      };
      *((unsigned int *) param1 = *((unsigned int *) local2 + 0x8) + 0xc) = param0;
      *((unsigned int *) local2 + 0x8) = param0;
      *((unsigned int *) param0 + 0x18) = 0x0;
      *((unsigned int *) param0 + 0xc) = local2;
      *((unsigned int *) param0 + 0x8) = param1;
      return;
    };
    *((unsigned int *) local5) = param0;
    *((unsigned int *) param0 + 0x18) = local3;
  };
  *((unsigned int *) param0 + 0xc) = param0;
  *((unsigned int *) param0 + 0x8) = param0;
}

// O[1] Decompilation of $func9, known as $func9
void $func9(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  long local5;

  global0 = local2 = (global0 - 0x30);
  if ((*((unsigned int *) param1) == -0x80000000)) {
    {
      local3 = *((unsigned int *) param1 + 0xc);
      *((unsigned int *) local4 = (local2 + 0x2c)) = 0x0;
      *((unsigned long *) local2 + 0x24) = 0x4294967296;
      $func3((local2 + 0x24), local3);
      *((unsigned int *) (local2 + 0x20)) = local3 = *((unsigned int *) local4);
      *((unsigned long *) local2 + 0x18) = local5 = *((unsigned long *) local2 + 0x24);
      *((unsigned int *) (param1 + 0x8)) = local3;
      *((unsigned long *) param1) = local5;
    };
  };
  local5 = *((unsigned long *) param1);
  *((unsigned long *) param1) = 0x4294967296;
  *((unsigned int *) local3 = (local2 + 0x10)) = *((unsigned int *) param1 = (param1 + 0x8));
  *((unsigned int *) param1) = 0x0;
  *((unsigned char *) 0x1002a5);
  *((unsigned long *) local2 + 0x8) = local5;
  if ((param1 = $func26(0xc, 0x4) == 0x0)) {
    {
      $func34(0x4, 0xc);
      abort("unreachable");
    };
  };
  *((unsigned long *) param1) = *((unsigned long *) local2 + 0x8);
  *((unsigned int *) (param1 + 0x8)) = *((unsigned int *) local3);
  *((unsigned int *) param0 + 0x4) = 0x1000bc;
  *((unsigned int *) param0) = param1;
  global0 = (local2 + 0x30);
}

// O[1] Decompilation of $func10, known as $func10
void $func10(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;

  global0 = local2 = (global0 - 0x20);
  label$1: {
    label$2: {
      if ((param1 = (param1 + 0x1) == 0x0)) break label$2;
      param1 = (local3 = ((unsigned) param1 <= 0x4) ? 0x4 : param1 = ((unsigned) param1 < local3) ? local3 = (local4 = *((unsigned int *) param0) << 0x1) : param1 << 0x2);
      local5 = (((unsigned) local3 < 0x20000000) << 0x2);
      label$3: {
        if ((local4 == 0x0)) {
          {
            *((unsigned int *) local2 + 0x18) = 0x0;
            break label$3;
          };
        };
        *((unsigned int *) local2 + 0x18) = 0x4;
        *((unsigned int *) local2 + 0x1c) = (local4 << 0x2);
        *((unsigned int *) local2 + 0x14) = *((unsigned int *) param0 + 0x4);
      };
      $func13((local2 + 0x8), local5, param1, (local2 + 0x14));
      param1 = *((unsigned int *) local2 + 0xc);
      if ((*((unsigned int *) local2 + 0x8) == 0x0)) {
        {
          *((unsigned int *) param0) = local3;
          *((unsigned int *) param0 + 0x4) = param1;
          break label$1;
        };
      };
      if ((param1 == -0x7fffffff)) break label$1;
      if ((param1 == 0x0)) break label$2;
      $func34(param1, *((unsigned int *) (local2 + 0x10)));
      abort("unreachable");
    };
    $func20();
    abort("unreachable");
  };
  global0 = (local2 + 0x20);
}

// O[1] Decompilation of $func11, known as $func11
void $func11(int param0, int param1, int param2, int param3, int param4, int param5) {
  // local index=6
  int local6;
  // local index=7
  int local7;

  global0 = local6 = (global0 - 0x20);
  *((unsigned int *) 0x1002dc) = (local7 = *((unsigned int *) 0x1002dc) + 0x1);
  label$1: {
    label$2: {
      if ((local7 < 0x0)) break label$2;
      if (*((unsigned char *) 0x1004a8)) break label$2;
      *((unsigned char *) 0x1004a8) = 0x1;
      *((unsigned int *) 0x1004a4) = (*((unsigned int *) 0x1004a4) + 0x1);
      *((unsigned char *) local6 + 0x1d) = param5;
      *((unsigned char *) local6 + 0x1c) = param4;
      *((unsigned int *) local6 + 0x18) = param3;
      *((unsigned int *) local6 + 0x14) = param2;
      *((unsigned int *) local6 + 0x10) = 0x100104;
      *((unsigned int *) local6 + 0xc) = 0x10001c;
      if ((param2 = *((unsigned int *) 0x1002cc) < 0x0)) break label$2;
      *((unsigned int *) 0x1002cc) = (param2 + 0x1);
      *((unsigned int *) 0x1002cc) = if (*((unsigned int *) 0x1002d4)) {
        {
          __function_table[*((unsigned int *) param1 + 0x10)](local6, param0);
          *((unsigned long *) local6 + 0xc) = *((unsigned long *) local6);
          __function_table[*((unsigned int *) *((unsigned int *) 0x1002d8) + 0x14)](*((unsigned int *) 0x1002d4), (local6 + 0xc));
          (*((unsigned int *) 0x1002cc) - 0x1);
        };
      } else {
        param2;
      };
      *((unsigned char *) 0x1004a8) = 0x0;
      if (param4) break label$1;
    };
    abort("unreachable");
  };
  abort("unreachable");
}

// O[1] Decompilation of $func12, known as $func12
void $func12(int param0, int param1, int param2) {
  // local index=3
  int local3;
  // local index=4
  int local4;

  global0 = local3 = (global0 - 0x20);
  label$1: {
    label$2: {
      if (((unsigned) param1 > param1 = (param1 + param2))) break label$2;
      param1 = ((local4 = ((unsigned) param1 <= 0x8) ? 0x8 : param1 = ((unsigned) param1 < local4) ? local4 = (param2 = *((unsigned int *) param0) << 0x1) : param1 ^ -0x1) >>> 0x1f);
      label$3: {
        if ((param2 == 0x0)) {
          {
            *((unsigned int *) local3 + 0x18) = 0x0;
            break label$3;
          };
        };
        *((unsigned int *) local3 + 0x1c) = param2;
        *((unsigned int *) local3 + 0x18) = 0x1;
        *((unsigned int *) local3 + 0x14) = *((unsigned int *) param0 + 0x4);
      };
      $func13((local3 + 0x8), param1, local4, (local3 + 0x14));
      param1 = *((unsigned int *) local3 + 0xc);
      if ((*((unsigned int *) local3 + 0x8) == 0x0)) {
        {
          *((unsigned int *) param0) = local4;
          *((unsigned int *) param0 + 0x4) = param1;
          break label$1;
        };
      };
      if ((param1 == -0x7fffffff)) break label$1;
      if ((param1 == 0x0)) break label$2;
      $func34(param1, *((unsigned int *) (local3 + 0x10)));
      abort("unreachable");
    };
    $func20();
    abort("unreachable");
  };
  global0 = (local3 + 0x20);
}

// O[2] Disassembly of $func13, known as $func13
void $func13(int param0, int param1, int param2, int param3) {
  // local index=4
  int local4;

  label$1: {
    label$2: {
      if (param1) {
        {
          if ((param2 < 0x0)) break label$2;
          if (param3 = label$4: {
            if (*((unsigned int *) param3 + 0x4)) {
              label$6: {
                if ((local4 = *((unsigned int *) (param3 + 0x8)) == 0x0)) {
                  break label$6;
                };
                break($func25(*((unsigned int *) param3), local4, param1, param2)) label$4;
              };
            };
            if ((param2 == 0x0)) break(param1) label$4;
            *((unsigned char *) 0x1002a5);
            $func26(param2, param1);
          }) {
            {
              *((unsigned int *) param0 + 0x4) = param3;
              *((unsigned int *) (param0 + 0x8)) = param2;
              *((unsigned int *) param0) = 0x0;
              return;
            };
          };
          *((unsigned int *) param0 + 0x4) = param1;
          *((unsigned int *) (param0 + 0x8)) = param2;
          break label$1;
        };
      };
      *((unsigned int *) param0 + 0x4) = 0x0;
      *((unsigned int *) (param0 + 0x8)) = param2;
      break label$1;
    };
    *((unsigned int *) param0 + 0x4) = 0x0;
  };
  *((unsigned int *) param0) = 0x1;
}

// O[1] Decompilation of $func14, known as $func14
void $func14(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  long local5;

  global0 = local2 = (global0 - 0x20);
  if ((*((unsigned int *) param1) == -0x80000000)) {
    {
      local3 = *((unsigned int *) param1 + 0xc);
      *((unsigned int *) local4 = (local2 + 0x1c)) = 0x0;
      *((unsigned long *) local2 + 0x14) = 0x4294967296;
      $func3((local2 + 0x14), local3);
      *((unsigned int *) (local2 + 0x10)) = local3 = *((unsigned int *) local4);
      *((unsigned long *) local2 + 0x8) = local5 = *((unsigned long *) local2 + 0x14);
      *((unsigned int *) (param1 + 0x8)) = local3;
      *((unsigned long *) param1) = local5;
    };
  };
  *((unsigned int *) param0 + 0x4) = 0x1000bc;
  *((unsigned int *) param0) = param1;
  global0 = (local2 + 0x20);
}

// O[1] Decompilation of $func15, known as $func15
void $func15(int param0, int param1) {
  global0 = param0 = (global0 - 0x30);
  if (*((unsigned char *) 0x1002a4)) {
    {
      *((unsigned long *) (param0 + 0x18)) = 0x1;
      *((unsigned int *) param0 + 0x10) = 0x2;
      *((unsigned int *) param0 + 0xc) = 0x100058;
      *((unsigned int *) param0 + 0x28) = 0x1;
      *((unsigned int *) param0 + 0x2c) = param1;
      *((unsigned int *) param0 + 0x14) = (param0 + 0x24);
      *((unsigned int *) param0 + 0x24) = (param0 + 0x2c);
      $func21((param0 + 0xc), 0x100080);
      abort("unreachable");
    };
  };
  global0 = (param0 + 0x30);
}

// O[2] Disassembly of $func16, known as $func16
int $func16(int param0, int param1, int param2) {
  // local index=3
  int local3;

  if (((unsigned) param2 > (*((unsigned int *) param0) - local3 = *((unsigned int *) param0 + 0x8)))) {
    {
      $func12(param0, local3, param2);
      local3 = *((unsigned int *) param0 + 0x8);
    };
  };
  $func35((*((unsigned int *) param0 + 0x4) + local3), param1, param2);
  *((unsigned int *) param0 + 0x8) = (param2 + local3);
  return 0x0;
}

// O[2] Disassembly of $func17, known as $func17
void $func17(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;

  *((unsigned char *) 0x1002a5);
  local2 = *((unsigned int *) param1 + 0x4);
  local3 = *((unsigned int *) param1);
  if ((param1 = $func26(0x8, 0x4) == 0x0)) {
    {
      $func34(0x4, 0x8);
      abort("unreachable");
    };
  };
  *((unsigned int *) param1 + 0x4) = local2;
  *((unsigned int *) param1) = local3;
  *((unsigned int *) param0 + 0x4) = 0x1000cc;
  *((unsigned int *) param0) = param1;
}

// O[2] Disassembly of $func18, known as $func18
export "__wbindgen_malloc"; // $func18 is exported to "__wbindgen_malloc"
int $func18(int param0, int param1) {
  label$1: {
    if (((__popcnt_i32(param1) != 0x1) | ((unsigned) (-0x80000000 - param1) < param0))) break label$1;
    if (param0) {
      {
        *((unsigned char *) 0x1002a5);
        if ((param1 = $func26(param0, param1) == 0x0)) break label$1;
      };
    };
    return param1;
  };
  abort("unreachable");
}

// O[2] Disassembly of $func19, known as $func19
int $func19(int param0, int param1, int param2, int param3) {
  label$1: {
    return label$2: {
      if ((param2 != 0x110000)) {
        if (__function_table[*((unsigned int *) param1 + 0x10)](param0, param2)) break(0x1) label$2;
      };
      if (param3) break label$1;
      0x0;
    };
  };
  return __function_table[*((unsigned int *) param1 + 0xc)](param0, param3, 0x0);
}

// O[1] Decompilation of $func20, known as $func20
void $func20() {
  // local index=0
  int local0;

  global0 = local0 = (global0 - 0x20);
  *((unsigned long *) (local0 + 0x14)) = 0x0;
  *((unsigned int *) local0 + 0xc) = 0x1;
  *((unsigned int *) local0 + 0x8) = 0x100144;
  *((unsigned int *) local0 + 0x10) = 0x100114 /* "library/alloc/src/raw_vec.rscapacity overflow" */;
  $func21((local0 + 0x8), 0x10014c);
  abort("unreachable");
}

// O[1] Decompilation of $func21, known as $func21
void $func21(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;

  global0 = local2 = (global0 - 0x20);
  *((unsigned short *) local2 + 0x1c) = 0x1;
  *((unsigned int *) local2 + 0x18) = param1;
  *((unsigned int *) local2 + 0x14) = param0;
  *((unsigned int *) local2 + 0x10) = 0x100188;
  *((unsigned int *) local2 + 0xc) = 0x10015c /* "called `Option::unwrap()` on a `None` value" */;
  global0 = param1 = (global0 - 0x10);
  if ((local2 = *((unsigned int *) param0 = (local2 + 0xc) + 0x8) == 0x0)) {
    {
      global0 = param0 = (global0 - 0x20);
      *((unsigned long *) (param0 + 0xc)) = 0x0;
      *((unsigned int *) param0 + 0x4) = 0x1;
      *((unsigned int *) param0 + 0x8) = 0x10015c /* "called `Option::unwrap()` on a `None` value" */;
      *((unsigned int *) param0 + 0x1c) = 0x2b;
      *((unsigned int *) param0 + 0x18) = 0x10015c /* "called `Option::unwrap()` on a `None` value" */;
      *((unsigned int *) param0) = (param0 + 0x18);
      $func21(param0, 0x1000ac);
      abort("unreachable");
    };
  };
  *((unsigned int *) param1 + 0xc) = *((unsigned int *) param0 + 0xc);
  *((unsigned int *) param1 + 0x8) = param0;
  *((unsigned int *) param1 + 0x4) = local2;
  global0 = param0 = (global0 - 0x10);
  local3 = *((unsigned int *) (local2 = *((unsigned int *) param1 = (param1 + 0x4)) + 0xc));
  label$2: {
    local3 = label$3: {
      label$4: {
        label$5: {
          switch (*((unsigned int *) local2 + 0x4)) {
            case 0: break label$5;
            case 1: break label$4;
            default: break label$2;
          };
        };
        if (local3) break label$2;
        local2 = 0x0;
        break(0x10001c) label$3;
      };
      if (local3) break label$2;
      local2 = *((unsigned int *) local3 = *((unsigned int *) local2) + 0x4);
      *((unsigned int *) local3);
    };
    *((unsigned int *) param0 + 0x4) = local2;
    *((unsigned int *) param0) = local3;
    $func11(param0, 0x1000dc, *((unsigned int *) param0 = *((unsigned int *) param1 + 0x4) + 0x8), *((unsigned int *) param1 + 0x8), *((unsigned char *) param0 + 0x10), *((unsigned char *) param0 + 0x11));
    abort("unreachable");
  };
  *((unsigned int *) param0 + 0xc) = local2;
  *((unsigned int *) param0) = -0x80000000;
  $func11(param0, 0x1000f0, *((unsigned int *) param0 = *((unsigned int *) param1 + 0x4) + 0x8), *((unsigned int *) param1 + 0x8), *((unsigned char *) param0 + 0x10), *((unsigned char *) param0 + 0x11));
  abort("unreachable");
}

// O[2] Disassembly of $func22, known as $func22
export "__wbindgen_realloc"; // $func22 is exported to "__wbindgen_realloc"
int $func22(int param0, int param1, int param2, int param3) {
  label$1: {
    if ((((__popcnt_i32(param3) != 0x1) | ((unsigned) (-0x80000000 - param3) < param1)) == 0x0)) {
      if (param0 = $func25(param0, param1, param3, param2)) break label$1;
    };
    abort("unreachable");
  };
  return param0;
}

// O[2] Disassembly of $func23, known as $func23
void $func23(int param0) {
  if (((*((unsigned int *) param0) | -0x80000000) != -0x80000000)) {
    $func2(*((unsigned int *) param0 + 0x4));
  };
}

// O[2] Disassembly of $func24, known as $func24
void $func24(int param0) {
  if (*((unsigned int *) param0)) {
    $func2(*((unsigned int *) param0 + 0x4));
  };
}

// O[2] Disassembly of $func25, known as $func25
int $func25(int param0, int param1, int param2, int param3) {
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;
  // local index=7
  int local7;
  // local index=8
  int local8;
  // local index=9
  int local9;

  label$2: {
    label$3: {
      label$4: {
        label$5: {
          if (((unsigned) param2 >= 0x9)) {
            {
              if (local8 = $func5(param2, param3)) break label$5;
              break(0x0) label$1;
            };
          };
          if (((unsigned) param3 > -0x10034)) break label$4;
          param1 = ((unsigned) param3 < 0xb) ? 0x10 : ((param3 + 0xb) & -0x8);
          local4 = (local5 = *((unsigned int *) param2 = (param0 - 0x4)) & -0x8);
          label$7: {
            if (((local5 & 0x3) == 0x0)) {
              {
                if (((((unsigned) param1 < 0x100) | ((unsigned) local4 < (param1 | 0x4))) | ((unsigned) (local4 - param1) >= 0x20001))) break label$7;
                break label$2;
              };
            };
            local7 = (local6 = (param0 - 0x8) + local4);
            label$9: {
              label$10: {
                label$11: {
                  label$12: {
                    if (((unsigned) param1 > local4)) {
                      {
                        if ((local7 == *((unsigned int *) 0x10048c))) break label$9;
                        if ((local7 == *((unsigned int *) 0x100488))) break label$11;
                        if ((local5 = *((unsigned int *) local7 + 0x4) & 0x2)) break label$7;
                        if (((unsigned) local4 = (local5 = (local5 & -0x8) + local4) < param1)) break label$7;
                        $func6(local7, local5);
                        if (((unsigned) param3 = (local4 - param1) < 0x10)) break label$12;
                        *((unsigned int *) param2) = ((param1 | (*((unsigned int *) param2) & 0x1)) | 0x2);
                        *((unsigned int *) param1 = (param1 + local6) + 0x4) = (param3 | 0x3);
                        *((unsigned int *) param2 = (local4 + local6) + 0x4) = (*((unsigned int *) param2 + 0x4) | 0x1);
                        $func4(param1, param3);
                        break label$2;
                      };
                    };
                    if (((unsigned) param3 = (local4 - param1) > 0xf)) break label$10;
                    break label$2;
                  };
                  *((unsigned int *) param2) = ((local4 | (*((unsigned int *) param2) & 0x1)) | 0x2);
                  *((unsigned int *) param1 = (local4 + local6) + 0x4) = (*((unsigned int *) param1 + 0x4) | 0x1);
                  break label$2;
                };
                if (((unsigned) local4 = (*((unsigned int *) 0x100480) + local4) < param1)) break label$7;
                label$14: {
                  if (((unsigned) param3 = (local4 - param1) <= 0xf)) {
                    {
                      *((unsigned int *) param2) = (((local5 & 0x1) | local4) | 0x2);
                      *((unsigned int *) param1 = (local4 + local6) + 0x4) = (*((unsigned int *) param1 + 0x4) | 0x1);
                      param3 = 0x0;
                      break label$14;
                    };
                  };
                  *((unsigned int *) param2) = ((param1 | (local5 & 0x1)) | 0x2);
                  *((unsigned int *) local8 = (param1 + local6) + 0x4) = (param3 | 0x1);
                  *((unsigned int *) param1 = (local4 + local6)) = param3;
                  *((unsigned int *) param1 + 0x4) = (*((unsigned int *) param1 + 0x4) & -0x2);
                };
                *((unsigned int *) 0x100488) = local8;
                *((unsigned int *) 0x100480) = param3;
                break label$2;
              };
              *((unsigned int *) param2) = ((param1 | (local5 & 0x1)) | 0x2);
              *((unsigned int *) param1 = (param1 + local6) + 0x4) = (param3 | 0x3);
              *((unsigned int *) local7 + 0x4) = (*((unsigned int *) local7 + 0x4) | 0x1);
              $func4(param1, param3);
              break label$2;
            };
            if (((unsigned) local4 = (*((unsigned int *) 0x100484) + local4) > param1)) break label$3;
          };
          if ((param1 = $func0(param3) == 0x0)) break label$4;
          break({
            local9 = $func35(param1, param0, ((unsigned) param1 < param3) ? param1 = ((param1 = *((unsigned int *) param2) & 0x3) ? -0x4 : -0x8 + (param1 & -0x8)) : param3);
            $func2(param0);
            local9;
          }) label$1;
        };
        $func35(local8, param0, ((unsigned) param1 < param3) ? param1 : param3);
        $func2(param0);
      };
      break(local8) label$1;
    };
    *((unsigned int *) param2) = ((param1 | (local5 & 0x1)) | 0x2);
    *((unsigned int *) param2 = (param1 + local6) + 0x4) = (param1 = (local4 - param1) | 0x1);
    *((unsigned int *) 0x100484) = param1;
    *((unsigned int *) 0x10048c) = param2;
    break(param0) label$1;
  };
  return param0;
}

// O[2] Disassembly of $func26, known as $func26
int $func26(int param0, int param1) {
  if (((unsigned) param1 >= 0x9)) {
    break($func5(param1, param0)) label$1;
  };
  return $func0(param0);
}

// O[2] Disassembly of $func27, known as $func27
void $func27(int param0, int param1) {
  *((unsigned long *) param0 + 0x8) = 0x7916663017593141705;
  *((unsigned long *) param0) = 0x8259774374431045597;
}

// O[2] Disassembly of $func28, known as $func28
void $func28(int param0, int param1) {
  *((unsigned long *) param0 + 0x8) = 0x8539995352090740368;
  *((unsigned long *) param0) = -0x5441813922324612405;
}

// O[2] Disassembly of $func29, known as $func29
void $func29(int param0, int param1) {
  *((unsigned long *) param0 + 0x8) = -0x163230743173927068;
  *((unsigned long *) param0) = -0x4493808902380553279;
}

// O[2] Disassembly of $func30, known as $func30
void $func30(int param0, int param1) {
  *((unsigned int *) param0 + 0x4) = 0x1000cc;
  *((unsigned int *) param0) = param1;
}

// O[2] Disassembly of $func31, known as $func31
int $func31(int param0, int param1) {
  *((unsigned int *) param0);
  while (1) break label$1;
}

// O[1] Decompilation of $func32, known as $func32
int $func32(int param0, int param1) {
  // local index=2
  int local2;
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;
  // local index=7
  int local7;
  // local index=8
  int local8;
  // local index=9
  int local9;
  // local index=10
  int local10;
  // local index=11
  int local11;
  // local index=12
  int local12;
  // local index=13
  long local13;
  // local index=14
  long local14;
  // local index=15
  int local15;
  // local index=16
  int local16;

  local13 = *((unsigned int *) param0);
  global0 = local5 = (global0 - 0x30);
  local2 = 0x27;
  label$1: {
    if (((unsigned) local13 < 0x10000)) {
      {
        local14 = local13;
        break label$1;
      };
    };
    while (1) {
      *((unsigned short *) (local4 = ((local5 + 0x9) + local2) - 0x4)) = *((unsigned short *) ((param0 = ((unsigned) (local3 = ((int) (local13 - (local14 = ((unsigned) local13 / 0x10000) * 0x10000))) & 0xffff) / 0x64) << 0x1) + 0x1001dc /* "0001020304050607080910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394959697989" */ ));
      *((unsigned short *) (local4 - 0x2)) = *((unsigned short *) ((((local3 - (param0 * 0x64)) & 0xffff) << 0x1) + 0x1001dc /* "0001020304050607080910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394959697989" */ ));
      local2 = (local2 - 0x4);
      if ({
        local15 = ((unsigned) local13 > 0x99999999);
        local13 = local14;
        local15;
      }) break label$3;
    break ;
    };
  };
  if (((unsigned) local3 = ((int) local14) > 0x63)) {
    *((unsigned short *) (local2 = (local2 - 0x2) + (local5 + 0x9))) = *((unsigned short *) ((((param0 = ((int) local14) - (local3 = ((unsigned) (param0 & 0xffff) / 0x64) * 0x64)) & 0xffff) << 0x1) + 0x1001dc /* "0001020304050607080910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394959697989" */ ));
  };
  label$5: {
    if (((unsigned) local3 >= 0xa)) {
      {
        *((unsigned short *) (local2 = (local2 - 0x2) + (local5 + 0x9))) = *((unsigned short *) ((local3 << 0x1) + 0x1001dc /* "0001020304050607080910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394959697989" */ ));
        break label$5;
      };
    };
    *((unsigned char *) (local2 = (local2 - 0x1) + (local5 + 0x9))) = (local3 + 0x30);
  };
  return {
    local16 = label$7: {
      local8 = ((local5 + 0x9) + local2);
      local6 = param0 = (local3 = *((unsigned int *) param1 + 0x1c) & 0x1) ? 0x2b : 0x110000;
      local10 = (param0 + local9 = (0x27 - local2));
      local7 = (local3 & 0x4) ? 0x10015c /* "called `Option::unwrap()` on a `None` value" */  : 0x0;
      label$8: {
        label$9: {
          if ((*((unsigned int *) param1) == 0x0)) {
            {
              param0 = 0x1;
              if ($func19(local2 = *((unsigned int *) param1 + 0x14), local3 = *((unsigned int *) param1 + 0x18), local6, local7)) break label$9;
              break label$8;
            };
          };
          if (((unsigned) local10 >= local11 = *((unsigned int *) param1 + 0x4))) {
            {
              param0 = 0x1;
              if ($func19(local2 = *((unsigned int *) param1 + 0x14), local3 = *((unsigned int *) param1 + 0x18), local6, local7)) break label$9;
              break label$8;
            };
          };
          if ((local3 & 0x8)) {
            {
              local3 = *((unsigned int *) param1 + 0x10);
              *((unsigned int *) param1 + 0x10) = 0x30;
              local2 = *((unsigned char *) param1 + 0x20);
              param0 = 0x1;
              *((unsigned char *) param1 + 0x20) = 0x1;
              if ($func19(local12 = *((unsigned int *) param1 + 0x14), local4 = *((unsigned int *) param1 + 0x18), local6, local7)) break label$9;
              param0 = ((local11 - local10) + 0x1);
              label$13: {
                while (1) {
                  if ((param0 = (param0 - 0x1) == 0x0)) break label$13;
                  if ((__function_table[*((unsigned int *) local4 + 0x10)](local12, 0x30) == 0x0)) break label$14;
                break ;
                };
                break(0x1) label$7;
              };
              param0 = 0x1;
              if (__function_table[*((unsigned int *) local4 + 0xc)](local12, local8, local9)) break label$9;
              *((unsigned char *) param1 + 0x20) = local2;
              *((unsigned int *) param1 + 0x10) = local3;
              param0 = 0x0;
              break label$9;
            };
          };
          local2 = (local11 - local10);
          label$15: {
            label$16: {
              label$17: {
                switch ((param0 = *((unsigned char *) param1 + 0x20) - 0x1)) {
                  case 0: break label$17;
                  case 1: break label$16;
                  case 2: break label$17;
                  default: break label$15;
                };
              };
              param0 = local2;
              local2 = 0x0;
              break label$15;
            };
            param0 = (local2 >>> 0x1);
            local2 = ((local2 + 0x1) >>> 0x1);
          };
          param0 = (param0 + 0x1);
          local4 = *((unsigned int *) (param1 + 0x18));
          local3 = *((unsigned int *) param1 + 0x10);
          param1 = *((unsigned int *) param1 + 0x14);
          label$18: {
            while (1) {
              if ((param0 = (param0 - 0x1) == 0x0)) break label$18;
              if ((__function_table[*((unsigned int *) local4 + 0x10)](param1, local3) == 0x0)) break label$19;
            break ;
            };
            break(0x1) label$7;
          };
          param0 = 0x1;
          if ($func19(param1, local4, local6, local7)) break label$9;
          if (__function_table[*((unsigned int *) local4 + 0xc)](param1, local8, local9)) break label$9;
          param0 = 0x0;
          while (1) {
            if ((param0 == local2)) break(0x0) label$7;
            param0 = (param0 + 0x1);
            if ((__function_table[*((unsigned int *) local4 + 0x10)](param1, local3) == 0x0)) break label$20;
          break ;
          };
          break(((unsigned) (param0 - 0x1) < local2)) label$7;
        };
        break(param0) label$7;
      };
      __function_table[*((unsigned int *) local3 + 0xc)](local2, local8, local9);
    };
    global0 = (local5 + 0x30);
    local16;
  };
}

// O[2] Disassembly of $func33, known as $func33
int $func33(int param0, int param1) {
  return $func3(param0, param1);
}

// O[2] Disassembly of $func34, known as $func34
void $func34(int param0, int param1) {
  __function_table[param0 ? param0 = *((unsigned int *) 0x1002c8) : 0x2](param0, param1);
  abort("unreachable");
}

// O[2] Disassembly of $func35, known as $func35
int $func35(int param0, int param1, int param2) {
  // local index=3
  int local3;
  // local index=4
  int local4;
  // local index=5
  int local5;
  // local index=6
  int local6;
  // local index=7
  int local7;
  // local index=8
  int local8;
  // local index=9
  int local9;

  label$1: {
    if (((unsigned) local4 = param2 < 0x10)) {
      {
        param2 = param0;
        break label$1;
      };
    };
    local5 = (param0 + local3 = ((0x0 - param0) & 0x3));
    if (local3) {
      {
        param2 = param0;
        local6 = param1;
        while (1) {
          *((unsigned char *) param2) = *((unsigned char *) local6);
          local6 = (local6 + 0x1);
          if (((unsigned) param2 = (param2 + 0x1) < local5)) break label$4;
        break ;
        };
      };
    };
    param2 = (local5 + local7 = (local8 = (local4 - local3) & -0x4));
    label$5: {
      if ((local3 = (param1 + local3) & 0x3)) {
        {
          if ((local7 <= 0x0)) break label$5;
          local9 = (local4 = (local3 << 0x3) & 0x18);
          param1 = (local6 = (local3 & -0x4) + 0x4);
          local4 = ((0x0 - local4) & 0x18);
          local6 = *((unsigned int *) local6);
          while (1) {
            *((unsigned int *) local5) = ((local6 >>> local9) | (local6 = *((unsigned int *) param1) << local4));
            param1 = (param1 + 0x4);
            if (((unsigned) local5 = (local5 + 0x4) < param2)) break label$7;
          break ;
          };
          break label$5;
        };
      };
      if ((local7 <= 0x0)) break label$5;
      param1 = local3;
      while (1) {
        *((unsigned int *) local5) = *((unsigned int *) param1);
        param1 = (param1 + 0x4);
        if (((unsigned) local5 = (local5 + 0x4) < param2)) break label$8;
      break ;
      };
    };
    local4 = (local8 & 0x3);
    param1 = (local3 + local7);
  };
  if (local4) {
    {
      local3 = (param2 + local4);
      while (1) {
        *((unsigned char *) param2) = *((unsigned char *) param1);
        param1 = (param1 + 0x1);
        if (((unsigned) param2 = (param2 + 0x1) < local3)) break label$10;
      break ;
      };
    };
  };
  return param0;
}

// O[2] Disassembly of $func36, known as $func36
void $func36(int param0) {}

// Function table
(*__function_table[20])() = {
  NULL,
  $func32, // $func32 i32 (i32, i32)
  $func15, // $func15 void (i32, i32)
  $func24, // $func24 void (i32)
  $func16, // $func16 i32 (i32, i32, i32)
  $func7, // $func7 i32 (i32, i32)
  $func33, // $func33 i32 (i32, i32)
  $func27, // $func27 void (i32, i32)
  $func36, // $func36 void (i32)
  $func29, // $func29 void (i32, i32)
  $func17, // $func17 void (i32, i32)
  $func30, // $func30 void (i32, i32)
  $func23, // $func23 void (i32)
  $func9, // $func9 void (i32, i32)
  $func14, // $func14 void (i32, i32)
  $func36, // $func36 void (i32)
  $func28, // $func28 void (i32, i32)
  $func31, // $func31 i32 (i32, i32)
  $func36, // $func36 void (i32)
  $func28, // $func28 void (i32, i32)
};
/****INITIALIZED MEMORY DUMP****/
// 00100000: 73 72 63 2f 6c 69 62 2e 72 73 00 00 00 00 10 00 : "src/lib.rs\x00\x00\x00\x00\x10\x00"
// 00100010: 0a 00 00 00 24 00 00 00 12 00 00 00 03 00 00 00 : "\n\x00\x00\x00$\x00\x00\x00\x12\x00\x00\x00\x03\x00\x00\x00"
// 00100020: 0c 00 00 00 04 00 00 00 04 00 00 00 05 00 00 00 : "\f\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00"
// 00100030: 06 00 00 00 6d 65 6d 6f 72 79 20 61 6c 6c 6f 63 : "\x06\x00\x00\x00memory alloc"
// 00100040: 61 74 69 6f 6e 20 6f 66 20 20 62 79 74 65 73 20 : "ation of  bytes "
// 00100050: 66 61 69 6c 65 64 00 00 34 00 10 00 15 00 00 00 : "failed\x00\x004\x00\x10\x00\x15\x00\x00\x00"
// 00100060: 49 00 10 00 0d 00 00 00 6c 69 62 72 61 72 79 2f : "I\x00\x10\x00\r\x00\x00\x00library/"
// 00100070: 73 74 64 2f 73 72 63 2f 61 6c 6c 6f 63 2e 72 73 : "std/src/alloc.rs"
// 00100080: 68 00 10 00 18 00 00 00 62 01 00 00 09 00 00 00 : "h\x00\x10\x00\x18\x00\x00\x00b\x01\x00\x00\t\x00\x00\x00"
// 00100090: 6c 69 62 72 61 72 79 2f 73 74 64 2f 73 72 63 2f : "library/std/src/"
// 001000a0: 70 61 6e 69 63 6b 69 6e 67 2e 72 73 90 00 10 00 : "panicking.rs�\x00\x10\x00"
// 001000b0: 1c 00 00 00 86 02 00 00 1e 00 00 00 03 00 00 00 : "\x1c\x00\x00\x00�\x02\x00\x00\x1e\x00\x00\x00\x03\x00\x00\x00"
// 001000c0: 0c 00 00 00 04 00 00 00 07 00 00 00 08 00 00 00 : "\f\x00\x00\x00\x04\x00\x00\x00\x07\x00\x00\x00\b\x00\x00\x00"
// 001000d0: 08 00 00 00 04 00 00 00 09 00 00 00 08 00 00 00 : "\b\x00\x00\x00\x04\x00\x00\x00\t\x00\x00\x00\b\x00\x00\x00"
// 001000e0: 08 00 00 00 04 00 00 00 0a 00 00 00 0b 00 00 00 : "\b\x00\x00\x00\x04\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00"
// 001000f0: 0c 00 00 00 10 00 00 00 04 00 00 00 0d 00 00 00 : "\f\x00\x00\x00\x10\x00\x00\x00\x04\x00\x00\x00\r\x00\x00\x00"
// 00100100: 0e 00 00 00 0f 00 00 00 00 00 00 00 01 00 00 00 : "\x0e\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00"
// 00100110: 10 00 00 00 6c 69 62 72 61 72 79 2f 61 6c 6c 6f : "\x10\x00\x00\x00library/allo"
// 00100120: 63 2f 73 72 63 2f 72 61 77 5f 76 65 63 2e 72 73 : "c/src/raw_vec.rs"
// 00100130: 63 61 70 61 63 69 74 79 20 6f 76 65 72 66 6c 6f : "capacity overflo"
// 00100140: 77 00 00 00 30 01 10 00 11 00 00 00 14 01 10 00 : "w\x00\x00\x000\x01\x10\x00\x11\x00\x00\x00\x14\x01\x10\x00"
// 00100150: 1c 00 00 00 3a 02 00 00 05 00 00 00 63 61 6c 6c : "\x1c\x00\x00\x00:\x02\x00\x00\x05\x00\x00\x00call"
// 00100160: 65 64 20 60 4f 70 74 69 6f 6e 3a 3a 75 6e 77 72 : "ed `Option::unwr"
// 00100170: 61 70 28 29 60 20 6f 6e 20 61 20 60 4e 6f 6e 65 : "ap()` on a `None"
// 00100180: 60 20 76 61 6c 75 65 00 12 00 00 00 00 00 00 00 : "` value\x00\x12\x00\x00\x00\x00\x00\x00\x00"
// 00100190: 01 00 00 00 13 00 00 00 69 6e 64 65 78 20 6f 75 : "\x01\x00\x00\x00\x13\x00\x00\x00index ou"
// 001001a0: 74 20 6f 66 20 62 6f 75 6e 64 73 3a 20 74 68 65 : "t of bounds: the"
// 001001b0: 20 6c 65 6e 20 69 73 20 20 62 75 74 20 74 68 65 : " len is  but the"
// 001001c0: 20 69 6e 64 65 78 20 69 73 20 00 00 98 01 10 00 : " index is \x00\x00�\x01\x10\x00"
// 001001d0: 20 00 00 00 b8 01 10 00 12 00 00 00 30 30 30 31 : " \x00\x00\x00�\x01\x10\x00\x12\x00\x00\x000001"
// 001001e0: 30 32 30 33 30 34 30 35 30 36 30 37 30 38 30 39 : "0203040506070809"
// 001001f0: 31 30 31 31 31 32 31 33 31 34 31 35 31 36 31 37 : "1011121314151617"
// 00100200: 31 38 31 39 32 30 32 31 32 32 32 33 32 34 32 35 : "1819202122232425"
// 00100210: 32 36 32 37 32 38 32 39 33 30 33 31 33 32 33 33 : "2627282930313233"
// 00100220: 33 34 33 35 33 36 33 37 33 38 33 39 34 30 34 31 : "3435363738394041"
// 00100230: 34 32 34 33 34 34 34 35 34 36 34 37 34 38 34 39 : "4243444546474849"
// 00100240: 35 30 35 31 35 32 35 33 35 34 35 35 35 36 35 37 : "5051525354555657"
// 00100250: 35 38 35 39 36 30 36 31 36 32 36 33 36 34 36 35 : "5859606162636465"
// 00100260: 36 36 36 37 36 38 36 39 37 30 37 31 37 32 37 33 : "6667686970717273"
// 00100270: 37 34 37 35 37 36 37 37 37 38 37 39 38 30 38 31 : "7475767778798081"
// 00100280: 38 32 38 33 38 34 38 35 38 36 38 37 38 38 38 39 : "8283848586878889"
// 00100290: 39 30 39 31 39 32 39 33 39 34 39 35 39 36 39 37 : "9091929394959697"
// 001002a0: 39 38 39 39 : "9899"
```
