using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main()
    {
        // Fájl beolvasása és adatok tárolása
        Dictionary<string, int> emberek = new Dictionary<string, int>();

        try
        {
            string[] sorok = File.ReadAllLines("emberek.txt");

            foreach (string sor in sorok)
            {
                string[] adatok = sor.Split(';');
                string nev = adatok[0];
                int eletkor = int.Parse(adatok[1]);

                emberek.Add(nev, eletkor);
            }
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("Hiba: emberek.txt fájl nem található!");
            Console.ReadLine();
            return;
        }

        // Név bekérése
        Console.Write("Kérem adja meg a nevet: ");
        string keresettNev = Console.ReadLine();

        // Életkor keresése
        if (emberek.ContainsKey(keresettNev))
        {
            int eletkor = emberek[keresettNev];
            Console.WriteLine("Az életkor: " + eletkor);
        }
        else
        {
            throw new NemTalalhatoNevException("Nincs ilyen név az emberek között!");
        }

        Console.ReadLine();
    }
}

// Saját kivétel osztály
class NemTalalhatoNevException : Exception
{
    public NemTalalhatoNevException(string message) : base(message)
    {
    }
}
