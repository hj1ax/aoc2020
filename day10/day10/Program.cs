using System;
using System.IO;
using System.Text;
using System.Linq;
using System.Collections.Generic;

namespace day10
{
    class Program
    {
        static string GetData(string filePath)
        {
            FileStream f = File.Open("input.txt", FileMode.Open);
            byte[] b = new byte[f.Length];
            UTF8Encoding temp = new UTF8Encoding(true);
            f.Read(b);
            return temp.GetString(b);
        }

        static void ResolvePart1()
        {
            int[] data = GetData("input.txt").Split("\n").Select(x => Int32.Parse(x)).ToArray();
            Array.Sort(data);
            int jolt1 = 0;
            int jolt3 = 0;
            int i = 0;
            int chargingOutlet = 0;
            foreach (int m in data)
            {
                int[] temp = data.TakeLast(data.Length - i).ToArray();
                foreach (int n in temp)
                {
                    if (Math.Abs(chargingOutlet - n) == 1)
                    {
                        jolt1++;
                        chargingOutlet = n;

                        break;
                    }
                    else if (Math.Abs(chargingOutlet - n) == 3)
                    {
                        jolt3++;
                        chargingOutlet = n;

                        break;
                    }

                    i++;
                }
            }

            jolt3++;

            Console.WriteLine($"Jolt1: {jolt1} Jolt3: {jolt3}");
            Console.WriteLine(jolt1 * jolt3);
        }

        static void ResolvePart2()
        {
            int[] data = GetData("input.txt").Split("\n").Select(x => Int32.Parse(x)).ToArray();
            Array.Sort(data);
            int jolt1 = 0;
            int jolt3 = 0;
            int i = 0;
            int chargingOutlet = 0;
            foreach (int m in data)
            {
                int[] temp = data.TakeLast(data.Length - i).ToArray();
                foreach (int n in temp)
                {
                    if (Math.Abs(chargingOutlet - n) == 1)
                    {
                        jolt1++;
                        chargingOutlet = n;

                        break;
                    }
                    else if (Math.Abs(chargingOutlet - n) == 3)
                    {
                        jolt3++;
                        chargingOutlet = n;

                        break;
                    }

                    i++;
                }
            }

            jolt3++;

            
        }

        static void Main(string[] args)
        {
            //ResolvePart1();
            ResolvePart2();
        }
    }
}
