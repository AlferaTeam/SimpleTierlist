document.addEventListener('DOMContentLoaded', function () {
    const categoryButtons = document.querySelectorAll('.category-btn');
    const contentArea = document.getElementById('content');

    const tierListData = {
        Vanilla: {
            1: [
                { name: "FourTure", status: "high", region: "ВСНГ" },
                { name: "s1ben", status: "low", region: "ЗСНГ" },
            ],
            2: [
                { name: "Bennifit", status: "high", region: "ВСНГ" },
                { name: "blqnki0", status: "high", region: "ЗСНГ" },
                { name: "stefypog", status: "low", region: "ВСНГ" },
            ],
            3: [
                { name: "AviKgolD1", status: "high", region: "ЗСНГ" },
                { name: "Shtyrlitz", status: "low", region: "ВСНГ" },
            ],
            4: [
                { name: "хз чесна", status: "low", region: "ЗСНГ" },
            ],
            5: [
                { name: "SlaveWs", status: "low", region: "ВСНГ" },
                { name: "RunishYT", status: "low", region: "ЗСНГ" },
            ],
        },
        Sword: {
            1: [
                { name: "Я", status: "high", region: "ВСНГ" },
            ],
            2: [
                { name: "не знаю", status: "low", region: "ЗСНГ" },
            ],
            3: [
                { name: "что", status: "high", region: "ВСНГ" },
            ],
            4: [
                { name: "тут", status: "low", region: "ЗСНГ" },
            ],
            5: [
                { name: "писать", status: "high", region: "ВСНГ" },
            ],
        },
        NethiritePot: {
            1: [
                { name: "Я", status: "high", region: "ЗСНГ" },
            ],
            2: [
                { name: "не знаю", status: "low", region: "ВСНГ" },
            ],
            3: [
                { name: "что", status: "high", region: "ЗСНГ" },
            ],
            4: [
                { name: "тут", status: "low", region: "ВСНГ" },
            ],
            5: [
                { name: "писать", status: "high", region: "ЗСНГ" },
            ],
        },
        UHC: {
            1: [
                { name: "Я", status: "high", region: "ВСНГ" },
            ],
            2: [
                { name: "не знаю", status: "low", region: "ЗСНГ" },
            ],
            3: [
                { name: "что", status: "high", region: "ВСНГ" },
            ],
            4: [
                { name: "тут", status: "low", region: "ЗСНГ" },
            ],
            5: [
                { name: "писать", status: "high", region: "ВСНГ" },
            ],
        },
        SMP: {
            1: [
                { name: "Я", status: "high", region: "ВСНГ" },
            ],
            2: [
                { name: "не знаю", status: "low", region: "ЗСНГ" },
            ],
            3: [
                { name: "что", status: "high", region: "ВСНГ" },
            ],
            4: [
                { name: "тут", status: "low", region: "ЗСНГ" },
            ],
            5: [
                { name: "писать", status: "high", region: "ВСНГ" },
            ],
        },
        Retired: {
            1: [
                { name: "Я", status: "high", region: "ЗСНГ" },
            ],
            2: [
                { name: "не знаю", status: "low", region: "ВСНГ" },
            ],
            3: [
                { name: "что", status: "high", region: "ЗСНГ" },
            ],
        },
        Blacklist: {
            1: [
                { name: "Я", status: "high", region: "ЗСНГ" },
            ],
            2: [
                { name: "не знаю", status: "low", region: "ВСНГ" },
            ],
            3: [
                { name: "что", status: "high", region: "ЗСНГ" },
            ],
            4: [
                { name: "тут", status: "low", region: "ВСНГ" },
            ],
            5: [
                { name: "писать", status: "high", region: "ЗСНГ" },
            ],
        },
    };

    function createTierList(data) {
        if (!data || Object.keys(data).length === 0) {
            return '<p>No data available for this category.</p>';
        }

        let html = '<table class="tier-list">';
        html += '<tr><th>TIER 1</th><th>TIER 2</th><th>TIER 3</th><th>TIER 4</th><th>TIER 5</th></tr>';

        const maxPlayers = Math.max(...Object.values(data).map(tier => tier.length));

        for (let i = 0; i < maxPlayers; i++) {
            html += '<tr>';
            for (let tier = 1; tier <= 5; tier++) {
                if (data[tier] && data[tier][i]) {
                    const player = data[tier][i];
                    const tierClass = player.status === 'high' ? 'high-tier' : player.status === 'low' ? 'low-tier' : 'banned-tier';
                    html += `
                        <td class="interactive ${tierClass}" data-player="${player.name}" data-status="${player.status}">
                            <div class="region-box">${player.region}</div>
                            ${player.name}
                        </td>`;
                } else {
                    html += '<td></td>';
                }
            }
            html += '</tr>';
        }

        html += '</table>';
        return html;
    }

    function createRetiredTable(data) {
        if (!data || Object.keys(data).length === 0) {
            return '<p>No data available for this category.</p>';
        }

        let html = '<table class="tier-list retired">';
        html += '<tr><th>TIER 1</th><th>TIER 2</th><th>TIER 3</th></tr>';

        const maxPlayers = Math.max(...Object.values(data).map(tier => tier.length));

        for (let i = 0; i < maxPlayers; i++) {
            html += '<tr>';
            for (let tier = 1; tier <= 3; tier++) {
                if (data[tier] && data[tier][i]) {
                    const player = data[tier][i];
                    const tierClass = player.status === 'high' ? 'high-tier' : 'low-tier';
                    html += `
                        <td class="interactive ${tierClass}" data-player="${player.name}" data-status="${player.status}">
                            <div class="region-box">${player.region}</div>
                            ${player.name}
                        </td>`;
                } else {
                    html += '<td></td>';
                }
            }
            html += '</tr>';
        }

        html += '</table>';
        return html;
    }

    function getPlayerTiers(playerName) {
        const playerTiers = [];
        for (const category in tierListData) {
            for (const tier in tierListData[category]) {
                const tierPlayers = tierListData[category][tier];
                for (const player of tierPlayers) {
                    if (player.name === playerName) {
                        playerTiers.push({ category, tier, status: player.status });
                    }
                }
            }
        }
        return playerTiers;
    }

    function createPlayerProfile(player) {
        const playerTiers = getPlayerTiers(player.name);

        while (playerTiers.length < 6) {
            playerTiers.push({ category: '', tier: '', status: '' });
        }

        const profileHTML = `
        <div class="profile-popup">
            <div class="profile-content">
                <button class="close-btn">&times;</button>
                <div class="profile-header">
                    <img src="https://mc-heads.net/avatar/${player.name}" alt="${player.name}'s skin" class="player-avatar">
                    <div class="player-info">
                        <h2>${player.name}</h2>
                        <div class="player-rank">Combat Master</div>
                        <div class="player-overall">#1 Overall (1488 Points)</div>
                    </div>
                </div>
                <div class="player-region">Region: ${player.region}</div>
                <div class="player-tiers">
                    ${createTierBoxes(playerTiers)}
                </div>
            </div>
        </div>
    `;

        document.body.insertAdjacentHTML('beforeend', profileHTML);

        const popup = document.querySelector('.profile-popup');
        const closeBtn = popup.querySelector('.close-btn');

        closeBtn.addEventListener('click', () => {
            popup.remove();
        });

        popup.addEventListener('click', (e) => {
            if (e.target === popup) {
                popup.remove();
            }
        });
    }

    // Создание блоков уровней
    function createTierBoxes(playerTiers) {
        if (playerTiers.length === 0) {
            return '<p>No tiers found for this player.</p>';
        }

        return playerTiers.map(tier => {
            const categoryIcon = getTierIcon(tier.category);

            const tierLabel = tier.status ? `${categoryIcon} ${tier.status === 'high' ? 'HT' : 'LT'}${tier.tier ? tier.tier : ''}` : '';

            const tierClass = tier.status === 'high' ? 'blue' : tier.status === 'low' ? 'red' : '';

            const emptyClass = tier.status ? '' : 'empty-tier';

            return `
            <div class="tier-box ${tierClass} ${emptyClass}">
                <div class="tier-label">
                    ${tierLabel}
                </div>
            </div>
        `;
        }).join('');
    }

    function getTierIcon(category) {
        const icons = {
            Vanilla: '🍞',
            Sword: '🗡️',
            NethiritePot: '⚔️',
            UHC: '🔨',
            SMP: '🌍',
            Retired: '🛋️',
            Blacklist: '🚫',
        };
        return icons[category] || '🎮';
    }

    function addTableCellClickHandlers() {
        const tableCells = document.querySelectorAll('.tier-list .interactive');
        tableCells.forEach(cell => {
            cell.addEventListener('click', function () {
                const playerName = this.dataset.player;
                const playerRegion = this.querySelector('.region-box').textContent;
                const playerStatus = this.dataset.status;
                createPlayerProfile({ name: playerName, region: playerRegion, status: playerStatus });
            });
        });
    }

    categoryButtons.forEach(button => {
        button.addEventListener('click', function () {
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const category = this.dataset.category;
            let categoryData = tierListData[category];

            let tableHTML = createTierList(categoryData);

            contentArea.innerHTML = `
                <h2>${category} Tier List</h2>
                ${tableHTML}
            `;
            addTableCellClickHandlers();
        });
    });

    categoryButtons[0].click();
});