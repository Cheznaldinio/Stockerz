import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 24

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shop Game")
clock = pygame.time.Clock()
start_string = "Welcome to Stockerz"

BiasesArray = [
    [
    "Concerns over data privacy and security breaches are casting a shadow over the once-thriving tech landscape.",
    "Several established tech firms are reporting declining revenues, signaling a potential downturn in the industry.",
    "Lingering supply chain disruptions are posing significant challenges to hardware manufacturers, impacting overall industry stability.",
    "Increasing regulatory scrutiny is creating headwinds for tech companies, leading to uncertainty and market volatility.",
    "Tech layoffs and downsizing efforts are on the rise, reflecting a broader contraction within the industry.",
    "Consumer confidence in emerging technologies is waning, contributing to a sluggish adoption rate for new products and services.",
    "Startups are facing difficulties securing funding, indicating a tightening financial environment for tech ventures.",
    "The failure of high-profile tech IPOs is dampening investor enthusiasm and eroding market confidence.",
    "Obsolete tech infrastructure is hindering the industry's ability to adapt to rapidly evolving market demands.",
    "Rising competition from non-tech companies entering the digital space is intensifying market saturation, triggering a potential downturn."
    "The latest breakthroughs in artificial intelligence are driving unprecedented innovation across various sectors.",
    "Investors are increasingly drawn to cutting-edge startups, signaling a positive shift in the tech investment landscape.",
    "Emerging technologies such as blockchain and quantum computing are gaining traction, promising a transformative future.",
    "The demand for skilled tech professionals is soaring, reflecting the industry's robust growth.",
    "Strategic partnerships between tech giants and smaller players are fostering a collaborative ecosystem poised for expansion.",
    "Venture capital funding is flowing into high-potential tech ventures, fueling the next wave of disruptive solutions.",
    "Cloud computing adoption is reaching new heights, streamlining operations and enhancing scalability for businesses.",
    "The proliferation of 5G networks is unlocking new possibilities, revolutionizing connectivity and communication.",
    "Tech companies are consistently outperforming market expectations, showcasing the resilience of the industry.",
    "The global tech ecosystem is witnessing a surge in M&A activity, indicating a buoyant phase of consolidation and growth."   
    ],
    [
    "Concerns about economic instability are impacting investor confidence negatively.",
    "Market volatility is on the rise, leading to increased uncertainty in finance.",
    "Stock prices are experiencing a downward trend, causing worry among investors.",
    "Analysts are cautious, warning of potential headwinds and a bearish market.",
    "Interest rates are on the rise, slowing down investment and economic activity.",
    "Corporate earnings are falling short of expectations, dampening market sentiment.",
    "Job cuts and layoffs in the financial sector are indicative of challenging times.",
    "Regulatory challenges are adding pressure to the finance industry, affecting growth.",
    "Trade tensions and geopolitical issues are casting a shadow on global financial markets.",
    "Mergers and acquisitions activity is slowing down, reflecting a lack of confidence.",
    "Investor optimism is on the rise as market indicators show positive trends.",
    "Economic indicators point towards sustained growth in the financial sector.",
    "Stock prices are steadily climbing, reflecting increased confidence among investors.",
    "Analysts predict a bullish market with strong potential for higher returns.",
    "Interest rates are declining, encouraging more investments and economic activity.",
    "Corporate earnings reports are exceeding expectations, boosting market sentiment.",
    "The job market in the financial sector is thriving, signaling a robust industry.",
    "Innovation and technology adoption are driving efficiency and growth in finance.",
    "Global markets are experiencing a synchronized upswing, benefitting the finance sector.",
    "Mergers and acquisitions activity is robust, indicating confidence in the market."
    ],
    [
    "Challenges in healthcare funding are impacting the industry's ability to innovate and expand.",
    "Regulatory uncertainties are creating a cautious atmosphere in the healthcare sector.",
    "Increasing healthcare costs are putting pressure on industry stakeholders and consumers.",
    "Drug pricing concerns and patent expirations are affecting the profitability of pharmaceutical companies.",
    "The healthcare workforce is facing shortages, leading to concerns about service quality.",
    "Public health crises are straining healthcare systems and causing disruptions in the industry.",
    "Consumer confidence in healthcare services is declining due to quality and accessibility issues.",
    "Political instability and policy changes are creating uncertainty for healthcare companies.",
    "Rising insurance premiums and out-of-pocket expenses are impacting patient affordability.",
    "Investor skepticism is growing amid concerns about the long-term sustainability of healthcare businesses.",
    "Medical breakthroughs and advancements in technology are driving growth in the healthcare sector.",
    "Increased funding for research and development is fostering innovation in healthcare.",
    "The demand for healthcare services is on the rise, creating opportunities for industry expansion.",
    "Pharmaceutical companies are experiencing a surge in drug approvals, contributing to industry growth.",
    "Investor confidence is bolstered by positive health outcomes and strong performance of healthcare stocks.",
    "Telemedicine adoption is increasing, enhancing accessibility and efficiency in healthcare services.",
    "Global collaboration on health initiatives is strengthening, leading to positive industry developments.",
    "Aging populations worldwide are driving demand for healthcare services and products.",
    "Healthcare companies are reporting strong financial results, reflecting a resilient industry.",
    "Government policies are supporting healthcare infrastructure, contributing to sector growth."
    ],
    [
    "Fluctuating oil prices and geopolitical tensions are causing uncertainty in the energy sector.",
    "Concerns about fossil fuel dependency and environmental issues are affecting industry sentiment.",
    "Investor confidence is waning amid regulatory uncertainties and policy changes.",
    "Energy companies are facing financial challenges due to oversupply and weak demand.",
    "Traditional energy sources are experiencing a decline in market share amid competition from renewables.",
    "Struggles with project financing and capital constraints are hindering energy infrastructure development.",
    "The global economic slowdown is impacting energy consumption and production.",
    "Supply chain disruptions are affecting the availability and affordability of energy resources.",
    "Energy companies are grappling with increased operational costs and reduced profit margins.",
    "The transition to renewable energy is presenting challenges for traditional fossil fuel industries.",
    "Renewable energy investments are surging, signaling a shift towards sustainable practices.",
    "Technological advancements in clean energy are driving growth in the energy sector.",
    "Government incentives and policies are supporting the expansion of renewable energy projects.",
    "Increased global demand for cleaner alternatives is boosting the renewable energy market.",
    "Investors are showing confidence in green energy companies, contributing to industry success.",
    "The adoption of electric vehicles is creating new opportunities for the energy sector.",
    "Oil prices are stabilizing, providing a favorable environment for energy companies.",
    "Strategic partnerships in the energy industry are fostering innovation and efficiency.",
    "Energy storage solutions are gaining traction, enhancing the reliability of renewable sources.",
    "International cooperation on climate goals is positively impacting the energy market."
    ],
    [
    "Brick-and-mortar stores are facing challenges with declining foot traffic and sales.",
    "Retailers are grappling with supply chain disruptions, impacting product availability.",
    "Consumer uncertainty is leading to cautious spending, affecting retail sales negatively.",
    "Intense competition and price wars are squeezing profit margins for retail businesses.",
    "Changing shopping habits and preferences are posing challenges for traditional retailers.",
    "Rising inflation and economic uncertainties are impacting consumer purchasing power.",
    "Retailers are experiencing increased operational costs, putting pressure on profitability.",
    "Store closures and bankruptcies are signs of a challenging environment for retail businesses.",
    "The shift to online shopping is causing challenges for traditional brick-and-mortar retailers.",
    "Retailers are struggling to adapt to rapidly changing market dynamics and consumer behavior.",
    "E-commerce sales are soaring, indicating a strong performance in the retail sector.",
    "Retailers are investing in online platforms, capitalizing on the growth of digital shopping.",
    "Consumer confidence is high, leading to increased spending and positive retail sales.",
    "Innovative technologies, such as AI and AR, are enhancing the customer shopping experience.",
    "Strategic marketing campaigns and loyalty programs are driving customer retention for retailers.",
    "The expansion of global markets is creating new opportunities for retail businesses.",
    "Retailers are adapting to changing consumer preferences, staying ahead of market trends.",
    "Investor interest in retail stocks is growing, reflecting optimism in the industry.",
    "Collaborations with influencers and celebrities are boosting brand visibility and sales.",
    "Sustainable and ethical practices in the retail sector are gaining consumer support."
    ],
    [
    "Competitive pricing pressures are impacting profit margins for telecom service providers.",
    "Regulatory challenges and changes in government policies are creating uncertainty in the industry.",
    "Consumer demand for traditional voice services is declining, affecting telecom revenues.",
    "Technological disruptions are posing challenges for legacy telecom business models.",
    "Telecom companies face increased cybersecurity threats, impacting customer trust.",
    "Saturation in mature markets is limiting the growth potential for telecom operators.",
    "Economic downturns are leading to reduced spending on telecom services by consumers and businesses.",
    "Increased competition from non-traditional players is disrupting the telecom market.",
    "The transition from hardware to software-based solutions is posing challenges for telecom equipment manufacturers.",
    "Telecom companies are experiencing challenges with infrastructure deployment and maintenance costs.",
    "5G infrastructure investments are driving growth and innovation in the telecom sector.",
    "Increased demand for high-speed internet is positively impacting telecom service providers.",
    "Telecom companies are expanding their network coverage, reaching more customers globally.",
    "The rise in remote work is boosting demand for telecom services and connectivity solutions.",
    "Strategic partnerships and mergers are strengthening the competitive position of telecom firms.",
    "Investments in fiber-optic networks are enhancing the speed and reliability of telecom services.",
    "Telecom operators are diversifying their services, offering bundled packages and value-added options.",
    "The Internet of Things (IoT) is creating new revenue streams for telecom companies.",
    "Government initiatives to bridge the digital divide are supporting the growth of telecom infrastructure.",
    "Telecom stocks are performing well, attracting investor confidence in the industry."
    ],
    [
    "Global economic uncertainties are impacting the demand for transportation services.",
    "Rising fuel prices are putting pressure on the profitability of transportation companies.",
    "Supply chain disruptions are causing challenges for shipping and logistics operations.",
    "Reduced travel and tourism due to global events are affecting the transport industry negatively.",
    "Air travel restrictions and safety concerns are impacting the aviation sector.",
    "Challenges with regulatory compliance are creating uncertainty for transport businesses.",
    "Transport companies are facing increased operational costs, affecting profit margins.",
    "Trade tensions and protectionist measures are impacting international shipping and trade.",
    "The shift towards remote work is leading to reduced demand for commuter transportation services.",
    "Technological disruptions, such as the rise of virtual meetings, are impacting travel-related industries.",
    "Global logistics and supply chain optimizations are boosting the transport sector.",
    "Investments in sustainable and electric transportation are driving positive change.",
    "Technological advancements in autonomous vehicles are revolutionizing the transportation industry.",
    "Increased international trade is leading to growth in shipping and freight services.",
    "Strategic partnerships and collaborations are enhancing efficiency in the transport sector.",
    "The expansion of e-commerce is driving demand for efficient last-mile delivery solutions.",
    "Government investments in infrastructure projects are supporting the growth of the transport industry.",
    "Innovative solutions such as hyperloop technology are creating new possibilities for transportation.",
    "The adoption of clean energy in aviation is contributing to positive environmental practices.",
    "Transportation companies are leveraging data analytics for improved route optimization and cost savings."
    ],
    [
    "Market uncertainties and regulatory challenges are impacting the profitability of utility companies.",
    "Fluctuating energy prices are creating challenges for revenue and budget planning in the utility sector.",
    "Natural disasters and extreme weather events are posing operational challenges for utilities.",
    "Aging infrastructure is creating reliability issues and maintenance challenges for utility services.",
    "Slow economic growth is affecting energy demand and putting pressure on utility revenues.",
    "Utilities are facing challenges with grid congestion and the integration of renewable energy sources.",
    "Increasing cybersecurity threats are posing risks to the reliability of utility services.",
    "Changes in government policies and regulations are creating uncertainty for utility companies.",
    "Utilities are grappling with the costs of complying with environmental regulations.",
    "The shift towards decentralized energy production is challenging traditional utility business models.",
    "Investments in renewable energy projects are driving growth in the utility sector.",
    "Government incentives and policies are promoting the transition to clean and sustainable utilities.",
    "Smart grid technology adoption is enhancing the efficiency and reliability of utility services.",
    "Increased demand for clean energy is creating new opportunities for utility companies.",
    "Utilities are investing in modernizing infrastructure to meet the growing energy needs.",
    "The integration of energy storage solutions is improving the stability of utility grids.",
    "Utilities are diversifying their energy sources, reducing reliance on traditional fossil fuels.",
    "Technological advancements in energy management systems are optimizing utility operations.",
    "Investor interest in green utilities is growing, reflecting a positive outlook for the industry.",
    "Utilities are actively participating in global efforts to reduce carbon emissions and combat climate change."
    ]
]

# Game variables
money = 100
#items = {
#    "Item 1": {"price": 10, "quantity": 0},
 #   "Item 2": {"price": 15, "quantity": 0},
  #  "Item 3": {"price": 20, "quantity": 0},
#    "Item 4": {"price": 25, "quantity": 0},
#    "Item 5": {"price": 30, "quantity": 0},
#    "Item 6": {"price": 35, "quantity": 0},
#    "Item 7": {"price": 40, "quantity": 0},
#    "Item 8": {"price": 45, "quantity": 0},
#}
day = 1
news = 0

items = ["Tech", "Finance", "Healthcare", "Energy", "Retail", "Telecom", "Transport", "Utilities"]
prices = [10, 15, 20, 25, 30, 35, 40, 45]
quantities = [0, 0, 0, 0, 0, 0, 0, 0]
bias = [0, 1, 0, 1, 0, 1, 0, 1]
font = pygame.font.SysFont(None, FONT_SIZE)

def stock(start_x, start_y, width, height, bias, name):
    pygame.draw.rect(screen, (100, 100, 100), (start_x, start_y, width, height))
    item_text = font.render(f"{name}", True, BLACK)
    screen.blit(item_text, (start_x + 2, start_y + 2))
    pygame.display.update()
    x = start_x
    y = start_y + height // 2
    up, down = -(height // 100), height // 100

    while x < (width + start_x):
        x += 1
        time.sleep(0.003)
        if y < start_y+5:
            y += random.randint(0, 6)
            screen.set_at((x, y), (255, 0, 0))
        elif y > start_y + height - 5:
            y += random.randint(-5, 0)
            screen.set_at((x, y), (255, 0, 0))
        else:
            if bias == 0 and random.randint(0, 4) == 0 and x > (start_x + (width // 2)):
                y += random.randint(0, 3)
            elif bias == 1 and random.randint(0, 4) == 0 and x > (start_x + (width // 2)):
                y += random.randint(-3, 0)
            y += random.randint(up, down)

            screen.set_at((x, y), (255, 0, 0))

        pygame.display.update()
    
    return 1 / (((y - start_y) / height + 0.5))

def draw_text(surface, font, text, box, color):
    font = pygame.font.SysFont(None, 18)
    words = text.split()
    max_width = box[2]
    max_height = box[3]
    x, y = box[0], box[1]
    lines = []
    current_line = []
    
    for word in words:
        # Check the width of the current line with the new word
        width, _ = font.size(' '.join(current_line + [word]))
        if width <= max_width-x:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))

    for line in lines:
        if y + font.get_height() <= box[1] + max_height:
            text_surface = font.render(line, True, color)
            surface.blit(text_surface, (x, y))
            y += font.get_height()
    font = pygame.font.SysFont(None, FONT_SIZE)

screen.fill(WHITE)
# Main game loop
run = True
while run:
    #screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT//2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display money
    money_text = font.render(f"Money: ${money}", True, BLACK)
    screen.blit(money_text, (10, 10))

    # Display items and their quantities
    item_y = 50
    item_x = 210
    for i in range(0,8):
        item_text = font.render(f"{items[i]}", True, BLACK)
        screen.blit(item_text, (10, item_y))
        item_text = font.render(f"{quantities[i]} x ${prices[i]} each", True, BLACK)
        screen.blit(item_text, (100, item_y))
        pygame.draw.rect(screen, BLACK, (item_x, item_y, 20, 20))
        plus_text = font.render("+", True, (200,200,200))
        screen.blit(plus_text, (item_x + 5, item_y))

        pygame.draw.rect(screen, BLACK, (item_x + 20, item_y, 20, 20))
        minus_text = font.render("-", True, WHITE)
        screen.blit(minus_text, (item_x + 25, item_y))

        item_y += 30
    
    font = pygame.font.SysFont(None, 60)
    pygame.draw.rect(screen, BLACK, (650, 20, 110, 40))
    play_text = font.render("PLAY", True, WHITE)
    screen.blit(play_text, (650,20))

    pygame.draw.rect(screen, BLACK, (350, 20, 120, 40))
    play_text = font.render(f"DAY {day}", True, WHITE)
    screen.blit(play_text, (350,20))

    font = pygame.font.SysFont(None, FONT_SIZE)

    pygame.draw.rect(screen, BLACK, (270, 80, 500, 200))
    pygame.draw.rect(screen, WHITE, (275, 85, 490, 190))
    if news != day:
        news = day
        start_string = "Day " + str(day) + " news: "
        numbers = list(range(8))

        # Shuffle the list in place
        random.shuffle(numbers)
        print(numbers)
        # Iterate over the shuffled list
        for i in numbers:
            bias[i] = random.randint(0,1)
            temp = bias[i] * 10 + random.randint(0, 9)
            
            print(i)
            print(temp)

            text = BiasesArray[i][temp]
            
            start_string += text
            start_string += " "
            
        text_box = (280, 90, 700, 270)
        
        pygame.display.update()
    
    draw_text(screen, font, start_string, text_box, BLACK)
    if day == 10:
        run = False

    money = round(money,3)
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if event.button == 1 and 650 <= x <= 760 and 20 <= y <= 60:
            day += 1
            y = HEIGHT//2
            x = 20
            for i in range(0,8):
                time.sleep(0.5)
                
                prices[i] = round(prices[i] * stock(x, y, 150, 100, bias[i],items[i]),1)
                
                if i == 3:
                    y += HEIGHT//4
                    x = 20
                else:
                    x += WIDTH//4
                money += prices[i] * quantities[i]
                quantities[i] = 0
            time.sleep(0.5)
        for i in range(0,8):
            button_y = 50 + 30 * i
            if event.button == 1:  # Left mouse button
                
                if item_x <= x <= item_x + 20 and button_y <= y <= button_y + 20 and money - prices[i] >= 0:  # Plus button
                    money = round(money - prices[i],1)
                    quantities[i] += 1
                    time.sleep(0.1)
                elif item_x + 20 <= x <= item_x + 40 and button_y <= y <= button_y + 20 and quantities[i] > 0:  # Minus button (if quantity > 0)
                    money = round(money + prices[i],1)
                    quantities[i] -= 1
                    time.sleep(0.05)
            
            
            
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)



font = pygame.font.Font(None, 100)
money_text = font.render(f"Money: ${money}", True, WHITE)
text_rect = money_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Display "Money" in the middle of the screen
screen.fill((0, 0, 0))  # Fill the screen with a black background
screen.blit(money_text, text_rect)
pygame.display.flip()

time.sleep(5)