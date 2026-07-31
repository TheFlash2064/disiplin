package com.example.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.example.ui.theme.*

data class ProphetDua(
    val prophet: String,
    val arabic: String,
    val turkishReading: String,
    val meaning: String,
    val source: String
)

val duas = listOf(
    ProphetDua(
        prophet = "Hz. Adem (as)",
        arabic = "رَبَّنَا ظَلَمْنَآ اَنْفُسَنَا وَاِنْ لَمْ تَغْفِرْ لَنَا وَتَرْحَمْنَا لَنَكُونَنَّ مِنَ الْخَاسِرٖينَ",
        turkishReading = "Rabbenâ zalemnâ enfusenâ ve in lem tagfir lenâ ve terhamnâ lenekûnenne minel-hâsirîn.",
        meaning = "Ey Rabbimiz! Biz kendimize zulmettik. Eğer bizi bağışlamaz, bize acımazsan mutlaka hüsrana uğrayanlardan oluruz.",
        source = "A'râf 7:23"
    ),
    ProphetDua(
        prophet = "Hz. Nuh (as)",
        arabic = "رَبِّ إِنِّي أَعُوذُ بِكَ أَنْ أَسْأَلَكَ مَا لَيْسَ لِي بِهِ عِلْمٌ ۖ وَإِلَّا تَغْفِرْ لِي وَتَرْحَمْنِي أَكُن مِّنَ الْخَاسِرِينَ",
        turkishReading = "Rabbi innî eûzu bike en es’eleke mâ leyse lî bihî ilm(ilmun), ve illâ tagfir lî ve terhamnî ekun minel hâsirîn(hâsirîne).",
        meaning = "Rabbim! Şüphesiz ben senden hakkında bilgim olmayan şeyi istemekten sana sığınırım. Eğer beni bağışlamaz ve bana acımazsan, şüphesiz ziyana uğrayanlardan olurum.",
        source = "Hûd 11:47"
    ),
    ProphetDua(
        prophet = "Hz. İbrahim (as)",
        arabic = "رَبِّ اجْعَلْنِي مُقِيمَ الصَّلَاةِ وَمِن ذُرِّيَّتِي ۚ رَبَّنَا وَتَقَبَّلْ دُعَاءِ",
        turkishReading = "Rabbic’alnî mukîmes salâti ve min zurriyyetî rabbenâ ve tekabbel duâ(duâi).",
        meaning = "Rabbim! Beni namaza devam eden bir kimse eyle. Soyumdan da böyle kimseler yarat. Rabbimiz! Duamı kabul eyle.",
        source = "İbrâhîm 14:40"
    ),
    ProphetDua(
        prophet = "Hz. Yusuf (as)",
        arabic = "فَاطِرَ السَّمَاوَاتِ وَالْأَرْضِ أَنتَ وَلِيِّي فِي الدُّنْيَا وَالْآخِرَةِ ۖ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ",
        turkishReading = "Fâtıras semâvâti vel ardı ente veliyyî fîd dunyâ vel âhırati, teveffenî muslimen ve elhıknî bis sâlihîn(sâlihîne).",
        meaning = "Ey gökleri ve yeri yaratan! Dünyada ve ahirette sen benim velimsin. Benim canımı müslüman olarak al ve beni iyilere kat.",
        source = "Yûsuf 12:101"
    ),
    ProphetDua(
        prophet = "Hz. Eyyub (as)",
        arabic = "أَنِّي مَسَّنِيَ الضُّرُّ وَأَنتَ أَرْحَمُ الرَّاحِمِينَ",
        turkishReading = "Ennî messeniyeḍ-ḍurru ve ente erhamur-râhimîn.",
        meaning = "Bana gerçekten hastalık isabet etti. Sen merhametlilerin en merhametlisisin.",
        source = "Enbiyâ 21:83"
    ),
    ProphetDua(
        prophet = "Hz. Musa (as)",
        arabic = "رَبِّ إِنِّي لِمَا أَنزَلْتَ إِلَيَّ مِنْ خَيْرٍ فَقِيرٌ",
        turkishReading = "Rabbi innî limâ enzelte ileyye min hayrin fakîr.",
        meaning = "Rabbim! Bana göndereceğin her hayra muhtacım.",
        source = "Kasas 28:24"
    ),
    ProphetDua(
        prophet = "Hz. Süleyman (as)",
        arabic = "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ الَّتِي أَنْعَمْتَ عَلَيَّ وَعَلَىٰ وَالِدَيَّ وَأَنْ أَعْمَلَ صَالِحًا تَرْضَاهُ وَأَدْخِلْنِي بِرَحْمَتِكَ فِي عِبَادِكَ الصَّالِحِينَ",
        turkishReading = "Rabbi evzı’nî en eşkure ni’metekelletî en’amte aleyye ve alâ vâlideyye ve en a’mele sâlihan terdâhu ve edhılnî bi rahmetike fî ibâdikes sâlihîn(sâlihîne).",
        meaning = "Rabbim! Bana ve anne babama verdiğin nimetlere şükretmemi, senin razı olacağın salih amel işlememi bana ilham et. Ve beni rahmetinle salih kullarının arasına kat.",
        source = "Neml 27:19"
    ),
    ProphetDua(
        prophet = "Hz. Zekeriyya (as)",
        arabic = "رَبِّ لَا تَذَرْنِي فَرْدًا وَأَنتَ خَيْرُ الْوَارِثِينَ",
        turkishReading = "Rabbi lâ tezernî ferden ve ente hayrul vârisîn(vârisîne).",
        meaning = "Rabbim! Beni tek başıma bırakma. Sen varislerin en hayırlısısın.",
        source = "Enbiyâ 21:89"
    ),
    ProphetDua(
        prophet = "Hz. Yunus (as)",
        arabic = "لَّآ إِلٰهَ إِلَّآ أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ",
        turkishReading = "Lâ ilâhe illâ ente subhâneke innî kuntu minez-zâlimîn.",
        meaning = "Senden başka ilâh yoktur. Seni her türlü noksanlıktan tenzih ederim. Gerçekten ben zalimlerden oldum.",
        source = "Enbiyâ 21:87"
    ),
    ProphetDua(
        prophet = "Hz. İsa (as)",
        arabic = "اللَّهُمَّ رَبَّنَا أَنزِلْ عَلَيْنَا مَائِدَةً مِّنَ السَّمَاءِ تَكُونُ لَنَا عِيدًا لِّأَوَّلِنَا وَآخِرِنَا وَآيَةً مِّنكَ ۖ وَارْزُقْنَا وَأَنتَ خَيْرُ الرَّازِقِينَ",
        turkishReading = "Allâhumme rabbenâ enzil aleynâ mâideten mines semâi tekûnu lenâ îden li evvelinâ ve âhırinâ ve âyeten minke, verzuknâ ve ente hayrur râzikîn(râzikîne).",
        meaning = "Ey Allah'ım! Ey Rabbimiz! Bize gökten bir sofra indir ki, bizim için, geçmiş ve geleceklerimiz için bayram ve senden bir mucize olsun. Bizi rızıklandır. Sen rızık verenlerin en hayırlısısın.",
        source = "Mâide 5:114"
    ),
    ProphetDua(
        prophet = "Hz. Muhammed (sav)",
        arabic = "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
        turkishReading = "Rabbenâ âtinâ fîd dunyâ haseneten ve fîl âhırati haseneten ve kınâ azâben nâr(nâri).",
        meaning = "Rabbimiz! Bize dünyada da iyilik ver, ahirette de iyilik ver ve bizi cehennem azabından koru.",
        source = "Bakara 2:201"
    )
)


@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProphetDuasScreen(navController: NavController) {
    var selectedGoal by remember { mutableStateOf(0) } // 0 = no goal, 1 = 1 dua/week, etc.

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Peygamber Duaları", color = MaterialTheme.colorScheme.onBackground) },
                navigationIcon = {
                    IconButton(onClick = { navController.popBackStack() }) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back", tint = MaterialTheme.colorScheme.onBackground)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.background
                )
            )
        },
        containerColor = MaterialTheme.colorScheme.background
    ) { padding ->
        LazyColumn(
            contentPadding = padding,
            verticalArrangement = Arrangement.spacedBy(16.dp),
            modifier = Modifier.padding(horizontal = 16.dp)
        ) {
            item {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clip(RoundedCornerShape(16.dp))
                        .background(MaterialTheme.colorScheme.surface)
                        .padding(16.dp)
                ) {
                    Text("Haftalık Ezber Programı", fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onBackground)
                    Spacer(modifier = Modifier.height(8.dp))
                    Text("Her hafta kaç dua ezberlemek istersiniz?", fontSize = 12.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                    Spacer(modifier = Modifier.height(16.dp))
                    
                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        (1..3).forEach { count ->
                            val isSelected = selectedGoal == count
                            Box(
                                modifier = Modifier
                                    .weight(1f)
                                    .clip(RoundedCornerShape(8.dp))
                                    .background(if (isSelected) AccentGreen else MaterialTheme.colorScheme.surfaceVariant)
                                    .clickable { selectedGoal = count }
                                    .padding(12.dp),
                                contentAlignment = Alignment.Center
                            ) {
                                Text("$count Dua", color = if (isSelected) Color.White else MaterialTheme.colorScheme.onBackground, fontWeight = FontWeight.Medium)
                            }
                        }
                    }
                    
                    if (selectedGoal > 0) {
                        Spacer(modifier = Modifier.height(16.dp))
                        Text(
                            "Bu haftaki hedefin: ${duas.first().prophet} duasını ezberlemek.",
                            color = AccentGreen,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Medium
                        )
                    }
                }
            }

            items(duas) { dua ->
                DuaCard(dua)
            }
            item { Spacer(modifier = Modifier.height(32.dp)) }
        }
    }
}

@Composable
fun DuaCard(dua: ProphetDua) {
    var expanded by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(16.dp))
            .background(MaterialTheme.colorScheme.surface)
            .clickable { expanded = !expanded }
            .padding(16.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(
                text = dua.prophet,
                fontWeight = FontWeight.Bold,
                fontSize = 18.sp,
                color = MaterialTheme.colorScheme.onBackground
            )
            Text(
                text = dua.source,
                fontSize = 12.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
        
        Spacer(modifier = Modifier.height(16.dp))
        
        Text(
            text = dua.arabic,
            fontSize = 24.sp,
            color = MaterialTheme.colorScheme.onBackground,
            modifier = Modifier.align(Alignment.End)
        )
        
        if (expanded) {
            Spacer(modifier = Modifier.height(16.dp))
            Text(
                text = dua.turkishReading,
                fontStyle = FontStyle.Italic,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                fontSize = 14.sp
            )
            Spacer(modifier = Modifier.height(8.dp))
            Text(
                text = dua.meaning,
                color = MaterialTheme.colorScheme.onBackground,
                fontSize = 14.sp
            )
            
            Spacer(modifier = Modifier.height(16.dp))
            
            var isFavorite by remember { mutableStateOf(false) }
            var isMemorized by remember { mutableStateOf(false) }
            
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Row(
                    modifier = Modifier
                        .clip(RoundedCornerShape(8.dp))
                        .clickable { isFavorite = !isFavorite }
                        .padding(8.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(4.dp)
                ) {
                    Text(if (isFavorite) "❤️" else "🤍", fontSize = 16.sp)
                    Text(if (isFavorite) "Favorilerde" else "Favoriye Ekle", fontSize = 12.sp, color = MaterialTheme.colorScheme.onBackground)
                }
                
                Row(
                    modifier = Modifier
                        .clip(RoundedCornerShape(8.dp))
                        .background(if (isMemorized) AccentGreen.copy(alpha = 0.2f) else MaterialTheme.colorScheme.surfaceVariant)
                        .clickable { isMemorized = !isMemorized }
                        .padding(horizontal = 12.dp, vertical = 8.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(4.dp)
                ) {
                    Text(if (isMemorized) "✅" else "📖", fontSize = 16.sp)
                    Text(if (isMemorized) "Ezberlendi" else "Ezberle", fontSize = 12.sp, color = if (isMemorized) AccentGreen else MaterialTheme.colorScheme.onBackground, fontWeight = FontWeight.Medium)
                }
            }
        }
    }
}
