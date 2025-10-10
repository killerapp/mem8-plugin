import React, { useState } from 'react';

// ============================================================================
// DATA MODELS
// ============================================================================

interface Command {
  id: string;
  name: string;
  complexity: number;
  tier: string;
  description: string;
  parallelization: 'none' | 'light' | 'heavy';
  agents?: string[];
  tools: string[];
  contextUsage: 'low' | 'medium' | 'high';
  autonomy: number;
  lines: number;
}

const commands: Command[] = [
  {
    id: 'local-review',
    name: 'm8-local-review',
    complexity: 3,
    tier: 'Setup & Utility',
    description: 'Git worktree setup with conditionals',
    parallelization: 'none',
    tools: ['Bash(git:*)', 'Bash(make:*)', 'Bash(mem8:*)'],
    contextUsage: 'low',
    autonomy: 3,
    lines: 50,
  },
  {
    id: 'commit',
    name: 'm8-commit',
    complexity: 3,
    tier: 'Setup & Utility',
    description: 'Analyze and create commits',
    parallelization: 'none',
    tools: ['Bash(git:*)'],
    contextUsage: 'low',
    autonomy: 3,
    lines: 44,
  },
  {
    id: 'plan',
    name: 'm8-plan',
    complexity: 4,
    tier: 'Workflow Automation',
    description: 'Synthesis & documentation',
    parallelization: 'none',
    tools: ['Read', 'Write', 'Bash(git:*)', 'Task'],
    contextUsage: 'medium',
    autonomy: 4,
    lines: 87,
  },
  {
    id: 'implement',
    name: 'm8-implement',
    complexity: 5,
    tier: 'Implementation Orchestration',
    description: 'Multi-phase implementation',
    parallelization: 'light',
    tools: ['Read', 'Write', 'Edit', 'Bash', 'Task'],
    contextUsage: 'high',
    autonomy: 5,
    lines: 71,
  },
  {
    id: 'describe-pr',
    name: 'm8-describe-pr',
    complexity: 6,
    tier: 'Multi-System Integration',
    description: 'Multi-system integration',
    parallelization: 'light',
    tools: ['Read', 'Write', 'Bash(gh:*)', 'Bash(git:*)', 'Bash(mem8:*)', 'Bash(make:*)', 'Bash(npm:*)', 'Bash(pytest:*)'],
    contextUsage: 'medium',
    autonomy: 6,
    lines: 77,
  },
  {
    id: 'debug',
    name: 'm8-debug',
    complexity: 7,
    tier: 'Parallel Investigation',
    description: '3 parallel investigation agents',
    parallelization: 'heavy',
    agents: ['Log Analyzer', 'DB Inspector', 'Git Inspector'],
    tools: ['Bash', 'Read', 'Task'],
    contextUsage: 'medium',
    autonomy: 7,
    lines: 200,
  },
  {
    id: 'validate',
    name: 'm8-validate',
    complexity: 8,
    tier: 'Forensic Verification',
    description: 'Forensic verification with 3+ agents',
    parallelization: 'heavy',
    agents: ['DB Verifier', 'Code Verifier', 'Test Verifier'],
    tools: ['Read', 'Task', 'Bash(make:*)', 'Bash(git:*)'],
    contextUsage: 'high',
    autonomy: 8,
    lines: 168,
  },
  {
    id: 'research',
    name: 'm8-research',
    complexity: 9,
    tier: 'Research Orchestration',
    description: '5+ parallel specialized agents',
    parallelization: 'heavy',
    agents: [
      'codebase-locator',
      'codebase-analyzer',
      'pattern-finder',
      'memory-locator',
      'memory-analyzer',
      'web-search-researcher',
    ],
    tools: ['Read', 'Task', 'Bash(mem8:*)', 'Bash(gh:*)', 'Bash(git:*)'],
    contextUsage: 'high',
    autonomy: 9,
    lines: 201,
  },
];

const workflows = {
  'Full Development Lifecycle': [
    { from: 'research', to: 'plan', label: '1→2' },
    { from: 'plan', to: 'implement', label: '2→3' },
    { from: 'implement', to: 'debug', label: '3→3a (if issues)' },
    { from: 'implement', to: 'validate', label: '3→4' },
    { from: 'validate', to: 'commit', label: '4→5' },
    { from: 'commit', to: 'describe-pr', label: '5→6' },
  ],
  'Quick Fix': [
    { from: 'debug', to: 'implement', label: '1→2' },
    { from: 'implement', to: 'commit', label: '2→3' },
    { from: 'commit', to: 'describe-pr', label: '3→4' },
  ],
  'Research Only': [
    { from: 'research', to: 'plan', label: '1→2 (optional)' },
  ],
  'Code Review': [
    { from: 'local-review', to: 'research', label: '1→2' },
    { from: 'research', to: 'validate', label: '2→3' },
  ],
};

// ============================================================================
// COMPONENTS
// ============================================================================

const CommandCard: React.FC<{ cmd: Command; selected: boolean; onClick: () => void }> = ({
  cmd,
  selected,
  onClick,
}) => {
  const tierColors = {
    'Setup & Utility': 'bg-blue-200',
    'Workflow Automation': 'bg-green-200',
    'Implementation Orchestration': 'bg-yellow-200',
    'Multi-System Integration': 'bg-orange-200',
    'Parallel Investigation': 'bg-red-200',
    'Forensic Verification': 'bg-purple-200',
    'Research Orchestration': 'bg-pink-200',
  };

  const parallelColors = {
    none: 'border-gray-400',
    light: 'border-yellow-500',
    heavy: 'border-red-500',
  };

  return (
    <div
      onClick={onClick}
      className={`
        cursor-pointer p-4 rounded-lg border-2 transition-all
        ${tierColors[cmd.tier as keyof typeof tierColors]}
        ${parallelColors[cmd.parallelization]}
        ${selected ? 'ring-4 ring-blue-500 scale-105' : 'hover:scale-102'}
      `}
    >
      <div className="font-bold text-sm mb-1">{cmd.name}</div>
      <div className="text-xs text-gray-700 mb-2">{cmd.description}</div>
      <div className="flex items-center justify-between text-xs">
        <span className="font-mono bg-white px-2 py-1 rounded">Complexity: {cmd.complexity}</span>
        {cmd.agents && (
          <span className="bg-red-100 px-2 py-1 rounded">{cmd.agents.length} agents</span>
        )}
      </div>
    </div>
  );
};

const ComplexityPyramid: React.FC<{ onSelectCommand: (id: string) => void }> = ({ onSelectCommand }) => {
  const levels = [
    { commands: ['research'], label: 'Research Orchestration' },
    { commands: ['validate'], label: 'Forensic Verification' },
    { commands: ['debug'], label: 'Parallel Investigation' },
    { commands: ['describe-pr'], label: 'Multi-System Integration' },
    { commands: ['implement'], label: 'Implementation Orchestration' },
    { commands: ['plan'], label: 'Workflow Automation' },
    { commands: ['commit', 'local-review'], label: 'Setup & Utility' },
  ];

  return (
    <div className="flex flex-col items-center space-y-2">
      {levels.map((level, idx) => (
        <div
          key={idx}
          className="flex justify-center space-x-2"
          style={{ width: `${100 - idx * 8}%` }}
        >
          {level.commands.map((cmdId) => {
            const cmd = commands.find((c) => c.id === cmdId)!;
            return (
              <div
                key={cmdId}
                onClick={() => onSelectCommand(cmdId)}
                className="flex-1 bg-gradient-to-b from-blue-400 to-blue-600 text-white p-3 rounded cursor-pointer hover:scale-105 transition-transform text-center"
                style={{ opacity: 1 - idx * 0.08 }}
              >
                <div className="font-bold text-sm">{cmd.name}</div>
                <div className="text-xs">({cmd.complexity})</div>
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
};

const WorkflowDiagram: React.FC<{ workflow: string }> = ({ workflow }) => {
  const flow = workflows[workflow as keyof typeof workflows];
  if (!flow) return null;

  return (
    <div className="flex flex-col items-center space-y-4">
      {flow.map((edge, idx) => {
        const fromCmd = commands.find((c) => c.id === edge.from);
        const toCmd = commands.find((c) => c.id === edge.to);
        const isDashed = edge.label.includes('optional') || edge.label.includes('if issues');

        return (
          <React.Fragment key={idx}>
            <div className="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-md text-center font-semibold">
              {fromCmd?.name}
            </div>
            <div className="flex flex-col items-center">
              <div
                className={`w-0.5 h-8 ${isDashed ? 'border-l-2 border-dashed border-gray-400' : 'bg-gray-400'
                  }`}
              />
              <div className="text-xs text-gray-600 bg-white px-2 py-1 rounded border border-gray-300">
                {edge.label}
              </div>
              <div
                className={`w-0.5 h-8 ${isDashed ? 'border-l-2 border-dashed border-gray-400' : 'bg-gray-400'
                  }`}
              />
            </div>
            {idx === flow.length - 1 && (
              <div className="bg-green-500 text-white px-6 py-3 rounded-lg shadow-md text-center font-semibold">
                {toCmd?.name}
              </div>
            )}
          </React.Fragment>
        );
      })}
    </div>
  );
};

const InteractionMatrix: React.FC = () => {
  const matrix: Record<string, string[]> = {
    'local-review': ['validate', 'research'],
    commit: ['describe-pr'],
    plan: ['implement'],
    implement: ['commit', 'describe-pr', 'debug', 'validate'],
    debug: ['plan', 'implement'],
    validate: ['commit', 'describe-pr', 'debug'],
    research: ['plan', 'implement'],
  };

  return (
    <div className="overflow-x-auto">
      <table className="w-full border-collapse text-xs">
        <thead>
          <tr>
            <th className="border p-2 bg-gray-200">Creates Input For →</th>
            {commands.map((cmd) => (
              <th key={cmd.id} className="border p-2 bg-gray-100 rotate-45 h-24">
                <div className="transform origin-left">{cmd.name.replace('m8-', '')}</div>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {commands.map((rowCmd) => (
            <tr key={rowCmd.id}>
              <td className="border p-2 font-semibold bg-gray-100">{rowCmd.name}</td>
              {commands.map((colCmd) => (
                <td
                  key={colCmd.id}
                  className={`border p-2 text-center ${rowCmd.id === colCmd.id
                      ? 'bg-gray-300'
                      : matrix[rowCmd.id]?.includes(colCmd.id)
                        ? 'bg-green-200 font-bold'
                        : 'bg-white'
                    }`}
                >
                  {rowCmd.id === colCmd.id
                    ? '-'
                    : matrix[rowCmd.id]?.includes(colCmd.id)
                      ? '✓'
                      : ''}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const CommandDetail: React.FC<{ cmd: Command }> = ({ cmd }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-lg border-2 border-blue-500">
      <h3 className="text-2xl font-bold mb-4">{cmd.name}</h3>

      <div className="grid grid-cols-2 gap-4 mb-4">
        <div>
          <div className="text-sm text-gray-600">Complexity</div>
          <div className="text-3xl font-bold text-blue-600">{cmd.complexity}/10</div>
        </div>
        <div>
          <div className="text-sm text-gray-600">Autonomy</div>
          <div className="text-3xl font-bold text-green-600">{cmd.autonomy}/10</div>
        </div>
        <div>
          <div className="text-sm text-gray-600">Lines of Code</div>
          <div className="text-2xl font-bold text-purple-600">{cmd.lines}</div>
        </div>
        <div>
          <div className="text-sm text-gray-600">Context Usage</div>
          <div className="text-2xl font-bold text-orange-600 capitalize">{cmd.contextUsage}</div>
        </div>
      </div>

      <div className="mb-4">
        <div className="text-sm font-semibold text-gray-700 mb-2">Description</div>
        <div className="text-gray-800">{cmd.description}</div>
      </div>

      <div className="mb-4">
        <div className="text-sm font-semibold text-gray-700 mb-2">Tier</div>
        <div className="inline-block bg-blue-100 px-3 py-1 rounded-full">{cmd.tier}</div>
      </div>

      <div className="mb-4">
        <div className="text-sm font-semibold text-gray-700 mb-2">Parallelization</div>
        <div className={`inline-block px-3 py-1 rounded-full capitalize ${cmd.parallelization === 'heavy'
            ? 'bg-red-200'
            : cmd.parallelization === 'light'
              ? 'bg-yellow-200'
              : 'bg-gray-200'
          }`}>
          {cmd.parallelization}
          {cmd.parallelization === 'heavy' && ' (Multi-Agent)'}
        </div>
      </div>

      {cmd.agents && (
        <div className="mb-4">
          <div className="text-sm font-semibold text-gray-700 mb-2">Agents ({cmd.agents.length})</div>
          <div className="flex flex-wrap gap-2">
            {cmd.agents.map((agent) => (
              <div key={agent} className="bg-purple-100 px-3 py-1 rounded-full text-sm">
                {agent}
              </div>
            ))}
          </div>
        </div>
      )}

      <div>
        <div className="text-sm font-semibold text-gray-700 mb-2">Tools ({cmd.tools.length})</div>
        <div className="flex flex-wrap gap-2">
          {cmd.tools.map((tool) => (
            <div key={tool} className="bg-gray-100 px-3 py-1 rounded-full text-xs font-mono">
              {tool}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

const ComplexityVsAutonomyPlot: React.FC<{ onSelectCommand: (id: string) => void }> = ({ onSelectCommand }) => {
  const maxComplexity = 10;
  const maxAutonomy = 10;

  return (
    <div className="relative bg-white p-8 rounded-lg shadow-lg" style={{ height: '500px' }}>
      {/* Y-axis label */}
      <div className="absolute left-0 top-1/2 transform -translate-y-1/2 -rotate-90 text-sm font-semibold text-gray-700">
        Autonomy (Can run independently)
      </div>

      {/* X-axis label */}
      <div className="absolute bottom-0 left-1/2 transform -translate-x-1/2 text-sm font-semibold text-gray-700">
        Complexity
      </div>

      {/* Plot area */}
      <div className="ml-12 mb-12 relative bg-gray-50 border-2 border-gray-300" style={{ height: '400px', width: 'calc(100% - 48px)' }}>
        {/* Grid lines */}
        {[...Array(11)].map((_, i) => (
          <React.Fragment key={i}>
            <div
              className="absolute w-full border-t border-gray-200"
              style={{ bottom: `${(i / 10) * 100}%` }}
            />
            <div
              className="absolute h-full border-l border-gray-200"
              style={{ left: `${(i / 10) * 100}%` }}
            />
          </React.Fragment>
        ))}

        {/* Command points */}
        {commands.map((cmd) => (
          <div
            key={cmd.id}
            onClick={() => onSelectCommand(cmd.id)}
            className="absolute transform -translate-x-1/2 -translate-y-1/2 cursor-pointer hover:scale-125 transition-transform"
            style={{
              left: `${(cmd.complexity / maxComplexity) * 100}%`,
              bottom: `${(cmd.autonomy / maxAutonomy) * 100}%`,
            }}
            title={cmd.name}
          >
            <div className="relative">
              <div className="w-4 h-4 bg-blue-600 rounded-full border-2 border-white shadow-lg" />
              <div className="absolute left-6 top-0 whitespace-nowrap bg-white px-2 py-1 rounded shadow-md text-xs font-semibold border border-gray-300">
                {cmd.name}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Y-axis labels */}
      <div className="absolute left-0 ml-8 h-full flex flex-col justify-between" style={{ height: '400px', marginTop: '8px' }}>
        {[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0].map((val) => (
          <div key={val} className="text-xs text-gray-600">
            {val}
          </div>
        ))}
      </div>

      {/* X-axis labels */}
      <div className="absolute bottom-0 mb-8 w-full flex justify-between ml-12" style={{ width: 'calc(100% - 48px)' }}>
        {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((val) => (
          <div key={val} className="text-xs text-gray-600">
            {val}
          </div>
        ))}
      </div>
    </div>
  );
};

// ============================================================================
// MAIN APP
// ============================================================================

const App: React.FC = () => {
  const [activeView, setActiveView] = useState<'pyramid' | 'workflows' | 'matrix' | 'scatter' | 'grid'>('pyramid');
  const [selectedCommand, setSelectedCommand] = useState<string | null>(null);
  const [selectedWorkflow, setSelectedWorkflow] = useState<string>('Full Development Lifecycle');

  const selectedCmd = commands.find((c) => c.id === selectedCommand);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-100 to-gray-200 p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold mb-2 text-gray-800">Command Complexity Visualizer</h1>
        <p className="text-gray-600 mb-8">Interactive exploration of mem8 command ecosystem</p>

        {/* View selector */}
        <div className="flex space-x-2 mb-8 bg-white p-2 rounded-lg shadow">
          {(['pyramid', 'workflows', 'matrix', 'scatter', 'grid'] as const).map((view) => (
            <button
              key={view}
              onClick={() => setActiveView(view)}
              className={`
                px-4 py-2 rounded font-semibold transition-all capitalize
                ${activeView === view
                  ? 'bg-blue-600 text-white shadow-md'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }
              `}
            >
              {view === 'pyramid' && '📊 Pyramid'}
              {view === 'workflows' && '🔄 Workflows'}
              {view === 'matrix' && '📋 Matrix'}
              {view === 'scatter' && '📈 Scatter Plot'}
              {view === 'grid' && '🎯 Grid'}
            </button>
          ))}
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main visualization area */}
          <div className="lg:col-span-2 bg-white p-6 rounded-lg shadow-lg">
            {activeView === 'pyramid' && (
              <div>
                <h2 className="text-2xl font-bold mb-4">Complexity Pyramid</h2>
                <p className="text-gray-600 mb-6">Commands arranged by complexity level (click to select)</p>
                <ComplexityPyramid onSelectCommand={setSelectedCommand} />
              </div>
            )}

            {activeView === 'workflows' && (
              <div>
                <h2 className="text-2xl font-bold mb-4">Workflow Patterns</h2>
                <div className="flex space-x-2 mb-6">
                  {Object.keys(workflows).map((workflow) => (
                    <button
                      key={workflow}
                      onClick={() => setSelectedWorkflow(workflow)}
                      className={`
                        px-3 py-1 rounded text-sm transition-all
                        ${selectedWorkflow === workflow
                          ? 'bg-blue-600 text-white'
                          : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }
                      `}
                    >
                      {workflow}
                    </button>
                  ))}
                </div>
                <WorkflowDiagram workflow={selectedWorkflow} />
              </div>
            )}

            {activeView === 'matrix' && (
              <div>
                <h2 className="text-2xl font-bold mb-4">Command Interaction Matrix</h2>
                <p className="text-gray-600 mb-6">Which commands create input for other commands</p>
                <InteractionMatrix />
              </div>
            )}

            {activeView === 'scatter' && (
              <div>
                <h2 className="text-2xl font-bold mb-4">Complexity vs Autonomy</h2>
                <p className="text-gray-600 mb-6">Higher autonomy = can discover context independently</p>
                <ComplexityVsAutonomyPlot onSelectCommand={setSelectedCommand} />
              </div>
            )}

            {activeView === 'grid' && (
              <div>
                <h2 className="text-2xl font-bold mb-4">All Commands</h2>
                <div className="grid grid-cols-2 gap-4">
                  {commands.map((cmd) => (
                    <CommandCard
                      key={cmd.id}
                      cmd={cmd}
                      selected={selectedCommand === cmd.id}
                      onClick={() => setSelectedCommand(cmd.id)}
                    />
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Detail panel */}
          <div className="lg:col-span-1">
            {selectedCmd ? (
              <CommandDetail cmd={selectedCmd} />
            ) : (
              <div className="bg-white p-6 rounded-lg shadow-lg text-center text-gray-500">
                <div className="text-6xl mb-4">👆</div>
                <p>Click on a command to see details</p>
              </div>
            )}
          </div>
        </div>

        {/* Legend */}
        <div className="mt-8 bg-white p-6 rounded-lg shadow-lg">
          <h3 className="font-bold mb-4">Legend</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div>
              <div className="font-semibold mb-2">Parallelization</div>
              <div className="space-y-1">
                <div className="flex items-center">
                  <div className="w-4 h-4 border-2 border-gray-400 mr-2" />
                  <span>None/Sequential</span>
                </div>
                <div className="flex items-center">
                  <div className="w-4 h-4 border-2 border-yellow-500 mr-2" />
                  <span>Light</span>
                </div>
                <div className="flex items-center">
                  <div className="w-4 h-4 border-2 border-red-500 mr-2" />
                  <span>Heavy (Multi-Agent)</span>
                </div>
              </div>
            </div>
            <div>
              <div className="font-semibold mb-2">Context Usage</div>
              <div className="space-y-1">
                <div className="flex items-center">
                  <div className="w-4 h-4 bg-green-300 mr-2" />
                  <span>Low</span>
                </div>
                <div className="flex items-center">
                  <div className="w-4 h-4 bg-yellow-300 mr-2" />
                  <span>Medium</span>
                </div>
                <div className="flex items-center">
                  <div className="w-4 h-4 bg-red-300 mr-2" />
                  <span>High</span>
                </div>
              </div>
            </div>
            <div>
              <div className="font-semibold mb-2">Complexity Ranges</div>
              <div className="space-y-1 text-xs">
                <div>1-2: Simple</div>
                <div>3-4: Medium</div>
                <div>5-6: Complex</div>
                <div>7-9: Very Complex</div>
              </div>
            </div>
            <div>
              <div className="font-semibold mb-2">Key Insights</div>
              <div className="space-y-1 text-xs">
                <div>• Research is most complex (9)</div>
                <div>• 3 commands use heavy parallelization</div>
                <div>• 8 total commands</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
