import { Heart, Shield, TrendingUp } from "lucide-react";
import BMICalculator from "@/components/BMICalculator";

const Index = () => {
  return (
    <div className="min-h-screen">
      {/* Header */}
      <header className="text-center py-16 px-4 relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-primary/5 via-accent/5 to-primary/5 animate-pulse-slow"></div>
        <div className="max-w-4xl mx-auto relative z-10">
          <div className="flex items-center justify-center mb-6 animate-slide-up">
            <div className="gradient-primary rounded-full p-4 mr-4 animate-float glow-primary">
              <Heart className="w-10 h-10 text-primary-foreground animate-pulse" />
            </div>
            <h1 className="text-5xl md:text-7xl font-bold bg-gradient-to-r from-primary via-accent to-primary bg-clip-text text-transparent animate-rainbow">
              BMI Health Calculator
            </h1>
          </div>
          <p className="text-xl md:text-2xl text-muted-foreground max-w-3xl mx-auto leading-relaxed font-medium animate-fade-in">
            Calculate your Body Mass Index with our vibrant, interactive tool and discover your health journey in full color! 
          </p>
        </div>
      </header>

      {/* Main Calculator Section */}
      <main className="px-4 pb-12">
        <div className="max-w-6xl mx-auto">
          <div className="grid lg:grid-cols-3 gap-8 items-start">
            {/* Info Cards */}
            <div className="lg:col-span-1 space-y-6 animate-slide-up">
              <div className="gradient-card backdrop-blur-sm rounded-2xl p-8 border border-white/20 shadow-xl glow-primary hover:scale-105 transition-all duration-300">
                <div className="flex items-center mb-6">
                  <div className="gradient-secondary rounded-full p-3 mr-4 animate-float">
                    <Shield className="w-7 h-7 text-white" />
                  </div>
                  <h3 className="text-xl font-bold bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">Accurate Results</h3>
                </div>
                <p className="text-muted-foreground font-medium leading-relaxed">
                  Our calculator uses the standard BMI formula (weight/height²) 
                  recognized by healthcare professionals worldwide.
                </p>
              </div>

              <div className="gradient-card backdrop-blur-sm rounded-2xl p-8 border border-white/20 shadow-xl glow-accent hover:scale-105 transition-all duration-300">
                <div className="flex items-center mb-6">
                  <div className="gradient-warning rounded-full p-3 mr-4 animate-float">
                    <TrendingUp className="w-7 h-7 text-white" />
                  </div>
                  <h3 className="text-xl font-bold bg-gradient-to-r from-accent to-primary bg-clip-text text-transparent">Health Categories</h3>
                </div>
                <p className="text-muted-foreground font-medium leading-relaxed">
                  Get instant feedback on your BMI category with personalized 
                  health insights and colorful visual feedback.
                </p>
              </div>
            </div>

            {/* Calculator */}
            <div className="lg:col-span-2 flex justify-center">
              <BMICalculator />
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-primary/10 via-accent/10 to-primary/10"></div>
        <div className="relative border-t border-white/20 backdrop-blur-sm">
          <div className="max-w-4xl mx-auto px-4 py-12 text-center">
            <p className="text-muted-foreground font-medium leading-relaxed bg-white/5 rounded-xl p-6 backdrop-blur-sm">
              <strong className="text-primary font-bold">Disclaimer:</strong> This BMI calculator is for informational purposes only. 
              Please consult with a healthcare professional for personalized medical advice.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Index;

