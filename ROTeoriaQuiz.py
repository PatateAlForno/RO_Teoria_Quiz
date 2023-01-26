
import string, random



NUM_QUESITI_PER_QUIZ = 10
QUESTITI = {
    " Quale è l'affermazione giusta?": [
        "se una matrice A contiene solo elementi pari a 0, 1 o -1, allora essa è totalmente unimodulare",
        "condizione necessaria affinchè una matrice A sia totalmente unimodulare \n\t è che essa contenga solo elementi pari a 0, 1 o -1",
        "condizione necessaria o sufficiente affinchè una matrice A sia totalmente unimodulare \n\t è che essa contenga solo elementi pari a 0, 1 o -1",
        "condizione sufficiente affinchè una matrice A sia totalmente unimodulare \n\t è che essa contenga solo elementi pari a 0, 1, o -1",
    ],
    "Nel metodo del simplesso, cosa può succedere se si incontra una soluzione di base degenere?": [
        "in assenza di regole anti-ciclo, si rischia di rimanere bloccati sullo stesso punto",
        "in assenza di regole anti-ciclo, si genere una soluzione inamissibile",
        "in assenza di regole anti-ciclo, si generano infinite soluzioni ottime",
        "in assenza di regole anti-ciclo, si cambia punto ma la base rimane la stessa",
    ],
    "In un problema di scheduling con più di una macchina, il makespan coincide con:": [
        "l'istante in cui si concludono tutte le operazioni di processamento dei job sulle macchine",
        "l'istante di inizio del processamento del job processato per ultimo",
        "il tempo di lavoro della macchina che inizia a lavorare per prima",
        "il tempo di lavoro della macchina che processa più job",

    ],
    "Dato un problema di Programmazione Lineare in forma standard, sia A ∈ Rᵐ*ⁿ la matrice dei vincoli (con m < n e rg(A) = m), \n"
    "e il vettore dei costi b ≥ 0 il vettore risorse. Il problema di prima fase verifica se: " :[
        "il problema di partenza è ammissibile o meno",
        "il problema di partenza ha soluzione ottima o meno",
        "il problema di partenza è illimitato o meno",
        "il problema di partenza ammette infinite soluzioni ottime o meno",
    ],
    "Sia dato un problema di Programmazione Lineare in forma standard, caratterizato dalla matrice dei vincoli \n"
    "A ∈ Rᵐ*ⁿ, con m < n e rg(A) = m. Sia x ∈ Rⁿ una soluzione di base. Allora: ": [
        "le colonne di A corrispondenti alle componenti non nulle di x̄ sono linearmente indipendenti",
        "le colonne di A corrispondenti alle componenti non nulle di x̄ sono linearmente dipendenti",
        "le colonne di A corrispondenti alle componenti non nulle di x sono linearmente dipendenti",
        "le colonne di A corrispondenti alle componenti non nulle di x sono linearmente indipendenti",

    ],
    "Dato il problema dei trasporti, sia a ∈ Rᵐ il vettore delle offerte nei nodi di origine e sia b ∈ Rⁿ il vettore \n"
    "delle domande nei nodi di destinazione. Qual è l'affermazione giusta?": [
        "\n                                            ₘ        ₙ\n"
        "    il problema è ammissibile se e solo se Σ   aᵢ = Σ   bⱼ\n"
        "                                            ᵢ=₁      ⱼ=₁            ",
        "\n                   ₘ        ₙ\n"
        "    la condizione Σ   aᵢ = Σ   bⱼ e solo sufficiente, ma non necessaria affinche il problema sia ammissibile\n"
        "                   ᵢ=₁      ⱼ=₁            ",
          "\n                                         ₘ        ₙ\n"
        "    se il problema e ammissibile allora Σ   aᵢ = Σ   bⱼ, ma non vale il viceversa\n"
        "                                         ᵢ=₁      ⱼ=₁            ",
          "\n        ₘ        ₙ\n"
        "    se Σ   aᵢ = Σ   bⱼ allora il problema e ammissibile, ma non vale il viceversa\n"
        "        ᵢ=₁      ⱼ=₁            ",
    ],
    "Dato un problema P di Programmazione Lineare Intera, allora:":[
        "la regione ammisibile di P e' contenuta nella regione ammissibile del suo rilassato continuo",
        "la regione ammissibile di P non si interseca mai con la regione ammissibile del suo rilassato continuo",
        "la regione ammissibile di P contiene la regione ammissibile del suo rilassato continuo",
        "la regione ammissible di P coincide sempre con la regione ammissibile del suo rilassato continuo",
    ],
    "Data una soluzione ammissibile per il primale e data una soluzione ammissibile per il duale, il teorema \n"
    "della complementarieta' primale-duale afferma che:": [
    "le due soluzioni soddisfano le relazioni di complementarieta' se e solo se sono ottime, \n\t rispettivamente, per il primale e per il duale",
    "se le due soluzioni sono ottime, rispettivamente, per il primale e per il duale, \n\t allora soddisfano le relazioni di complementarieta' (ma non vale il viceversa)",
    "se le due soluzioni soddisfano le relazioni di complementarieta' allora sia il primale \n\t che il duale ammettono infinite soluzioni ottime",
    "se le due soluzioni soddisfano le relazioni di complementarieta' allora esse sono ottime, \n\t rispettivamente per il primale e per il duale (ma non vale il viceversa",
    ],
    "Dato un problema di Programmazione Linerare, sia X la sua regione ammissibile. Allora: ":[
        "se il problema ha soluzione ottima, ne consegue che possiede almeno una soluzione ottima in corrispondenza di un punto estremo di X",
        "se il problema ha soluzione ottima, ne consegue che possiede una soluzione ottima solo in corrispondenza di un punto estremo di X",
        "se il problema ha soluzione ottima, ne consegue che possiede al massimo una soluzione ottima in corrispondenza di un punto estremo di X",
        "se il problema e' ammissibile, ne consegue che possiede almeno una soluzione ottima in corrispondenza di un punto estremo di X",
    ],
        "Nel metodo del simplesso, in corrispondenza della soluzione di base corrente x̄, il passo α e ottenibile con la \n"
     "                  x̄β(i)       \n"
    "formula α = min   ————— (scelta della riga del pivot). Tale formula garantisce:\n"
    "          i|d₁>0    dᵢ\n":[
        "che la nuova soluzione di base soddisfi i vincoli x > 0 ",
        "che la nuova soluzione di base soddisfi i vincoli x > 0 e Ax=b",
        "che la nuova soluzione di base soddisfi i vincoli Ax = b ",
        "che la nuova soluzione di base sia ottima ",
    ],
    "In un problema di scheduling, il tempo di rilascio di un job e':":[
        "l'istante a partire dal quale il job puo' essere processato",
        "l'istante di inizio del processamento del job",
        "l'istante in cui termina il processamento del job",
        "l'istante entro il quale deve essere processato il job",
    ],
    "Il problema del massimo flusso:":[
        "ammette sempre soluzione ottima",
        "puo' non avere soluzione ottima",
        "puo' essere illimitato, ma non puo' mai essere inammissibile",
        "puo' essere inammissibile, ma non puo' mai essere illimitato",
    ],
    "La formulazione ideale di un problema di Programmazione Lineare Intera si ha quando:":[
        "la sua regione ammissibile coincide con la copertura convessa della regione ammissibile del rilassato continuo",
        "la copertura convessa della sua regione ammissibile coincide con la regione ammissibile del rilassato continuo",
        "la sua regione ammissibile e' contenuta nella regione ammissibile del rilassato continuo",
        "la copertura convessa della sua regione ammissibile e' contenuta nella regione ammissibile del rilassato continuo",

    ],
    "Sia dato un problema di Programmazione Lineare in forma standard, caratterizzato dalla matrice dei vincoli \n"
    "A ∈ Rᵐ*ⁿ, con m < n e rg(A) = m. Le soluzioni di base sono:":[
        "in numero finito, pari al massimo a n!/m!(n-m)!",
        "in numero finito, pari a m!/n!(n-m)!",
        "in numero finito, pari al massimo a m!/n!(n-m)!",
        "in numero finito, pari a n!/m!(n-m)!",
    ],
    "Qual è l'affermazione giusta?":[
        "se il problema ammette soluzione ottima, il simplesso determina una soluzione ottima \n\t di base ricercandola fra le soluzioni ammissibili di base",
        "se il problema ammette soluzione ottima, il simplesso determina una soluzione ottima \n\t (anche non di base) ricercandola fra tutte le soluzioni ammissibili",
        "se il problema ammette soluzione ottima, il simplesso determina una soluzione ottima \n\t ricercandola fra tutte le soluzioni di base",
        "il simplesso determina una soluzione ottima di base, solo quando quest'ultima e' l'unica \n\t soluzione ottima del problema.",
    ],
    "Dato un problema di Programmazione Lineare in forma standard, sia A ∈ Rᵐ*ⁿ la matrice dei vincoli (con m < n \n"
    "e rg(A) = m), e il vettore dei costi b ≥ 0 il vettore risorse. Sia p* il valore ottimo di funzione obiettivo del \n"
    "problema di prima fase. Allora:":[
        "se p* > 0, il problema di partenza è inammissibile",
        "se p* = 0, il problema di partenza è illimitato",
        "se p* > 0, il problema di partenza è ammissibile",
        "se p* > 0, il problema di partenza è illimitato",
    ],
    "Una matrice A ∈ Rᵐ*ⁿ, con m < n, è definita totalmente unimodulare se:": [
        "ogni sua sottomatrice quadrata e invertibile, di qualsiasi ordine, ha determinante pari a 1 o -1",
        "qualche sua sottomatrice quadrata e invertibile, di ordine m, ha determinante pari a 1 o -1",
        "solo le sue sottomatrice quadrate e invertibili, di ordine n, hanno determinante pari a 1 o -1",
        "solo le sue sottomatrice quadrate e invertibili, di ordine m, hanno determinante pari a 1 o -1",
    ],
    "Dato un problema di Programmazione Lineare, sia X ≠ Ø la sua regione ammissibile. Allora:": [
        "X è un insieme convesso",
        "X puo' essere un insieme convesso",
        "X è un insieme concavo",
        "X non è un insieme convesso, nè concavo",
    ],
    "Qual è l'affermazione giusta?":[
        "la regione ammissibile di un problema di Programmazione Lineare Intera è contenuta nella regione ammissibile \n\t del rilassato continuo",
        "la regione ammissibile di un problema di Programmazione Lineare Intera contiene la regione ammissibile del \n\t rilassato continuo",
        "la regione ammissibile di un problema di Programmazione Lineare Intera non si interseca mai con la regione \n\t ammissibile del rilassato continuo",
        "la regione ammissibile di un problema di Programmazione Lineare Intera coincide sempre con la regione \n\t ammissibile del rilassato continuo"
     ],
     "Sia dato un problema di Programmazione Lineare in forma standard, caratterizzato dalla matrice dei vincoli\n"
     "A ∈ Rᵐ*ⁿ, con m < n e rg(A) = m. Un punto x̄ ∈ Rⁿ e' una soluzione di base degenere se:":[
        "almeno una componente in base e' nulla",
        "almeno una componente fuori base e' nulla",
        "esattamente una componente in base e' nulla",
        "tutte le componenti in base sono nulle",
     ],
        "Nel problema di flusso a costo minimo, sia d ∈ Rᵐ il vettore di divergenza. Allora:":[
        "\n                   m\n"
        "    la condizione Σ   dᵢ = 0  e' necessaria e sufficiente perche' il problema sia ammissibile.'\n"
        "                   ᵢ=₁",
        "\n                   m\n"
        "    la condizione Σ   dᵢ = 0  e' sufficiente, ma non necessaria, perche' il problema sia ammissibile.'\n"
        "                   ᵢ=₁",
        "\n                   m\n"
        "    la condizione Σ   dᵢ = 0  e' necessaria e sufficiente perche' il problema abbia soluzione ottima.'\n"
        "                   ᵢ=₁",
        "\n                   m\n"
        "    la condizione Σ   dᵢ = 0  e' necessaria, ma non sufficiente, perche' il problema sia ammissibile.'\n"
        "                   ᵢ=₁"
    ],
    "Dato un insieme convesso E ⊂ ℝⁿ, un punto 𝔀 ∈ E, e' un punto estremo se:": [
        "non esiste nessuna coppia di punti x, y ∈ E, con x ≠ y, tale che w = λx + (1 - λ)y, per qualche λ ∈ ]0,1[",
        "esistono infinite coppie di punti x, y ∈ E, tale che w = λx + (1-λ)y, per qualche λ ∈ ]0,1[",
        "esiste qualche coppia di punti x, y, com x ≠ y, tale che w = λx + (1 - λ)y, per qualche λ ∈ ]0,1[",
        "non esiste nessuna coppia di punti x, y, con x ≠ y, tale che w = λx + (1 - λ)y, per ogni λ ∈ [0,1]",
    ],
    "Sia dato un problema di Programmazione Lineare in forma standard, caratterizato dalla matrice dei vincoli \n"
    "A ∈ Rᵐ*ⁿ, con m < n e rg(A) = m. Sia x ∈ Rⁿ una soluzione di base. Allora: ": [
        "x̄ soddisfa sempre i vincoli Ax = b",
        "x̄ non soddisfa mai i vincoli Ax = b",
        "x̄ e' sempre ammissibile",
        "x̄ soddisfa sempre i vincoli x ≥ 0",
    ],
        "Dato un problema di Programmazione Lineare in forma standard, sia A ∈ Rᵐ*ⁿ la matrice dei vincoli (con m < n e rg(A) = m), \n"
    "e il vettore dei costi b ≥ 0 il vettore risorse. Il problema di prima fase verifica se: " :[
        "e' data dalla somma delle variabili artificiali",
        "coincide con la funzione obiettivo del problema di partenza",
        "e' data dal prodotto delle variabili artificiali",
        "coincide con la funzione obiettivo del problema di partenza, cambiata di segno",
    ],
    "In un problema di scheduling a singola macchina, nel caso statico e senza possibilita' di pre-emption, per \n"
    "minimizzare il tempo medio di completamento, quale regola si usa?":[
        "la stessa regola con cui si minimizza la somma pesata dei tempi di completamento, ponendo tutti i pesi uguale a 1",
        "la stessa regola con cui si minimizza il makespan",
        "la stessa regola con cui si minimizza il massimo ritardo",
        "la stessa regola con cui si minimizza il ritardo medio",
    ],
    "Il metodo del simplesso lavora nel seguente modo:":[
        "ricerca se esiste, una soluzione ottima fra le soluzioni ammissibili di base",
        "ricerca, se esiste, una soluzione ottima fra le soluzioni ammissibili",
        "ricerca, se esiste, una soluzione ottima fra le soluzioni di base",
        "ricerca, se esiste, una soluzione ottima fra i punti non estremi della regione ammissibile",
    ]



}

num_quesiti = min(NUM_QUESITI_PER_QUIZ, len(QUESTITI))
quesiti = random.sample(list(QUESTITI.items()), k=num_quesiti)
num_quesito_attuale = 0
num_corretti = 0

print("\n(っ◔◡◔)っ RO TEORIA, 10 DOMANDE PER QUIZ (っ◔◡◔)っ\n")
print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n")

for num, (quesito, alternative) in enumerate (quesiti, start=1):
    num_quesito_attuale += 1
    
    print(f"Quesito ({num_quesito_attuale}/{num_quesiti})")
    print(f"{quesito }")
    risposta_corretta = alternative[0]
    alternative_etichettate = dict(
        zip(string.digits, random.sample(alternative, k=len(alternative)))
        )
    for etichetta, alternativa in alternative_etichettate.items():
        print(f"  {etichetta}) {alternativa}")

    while (etichetta_risposta := input("\nrisposta? ")) not in alternative_etichettate:
        print(f"inserisci di nuovo")

    risposta = alternative_etichettate[etichetta_risposta]
    
    if risposta != risposta_corretta:
        print(f"Risposta errata. La risposta correta è: {risposta_corretta!r}\n")
        continue
		        
    num_corretti += 1
    print("⭐ Risposta corretta ⭐ \n")
        

print(f"✌(◕‿-)✌   RISULTATO: {num_corretti} / 10  ✌(◕‿-)✌ ")